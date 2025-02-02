from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from together import Together
import os
import streamlit as st
import time
import streamlit_lottie as st_lottie 

# # Streamlit Page Configuration
# st.set_page_config(page_title="Legal Offense Query System", layout="wide")

def render_page():

    # Streamlit Title
    st.markdown("<h1 class='header'>LegalQ</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='header'>A Legal Offense Query System</h3>", unsafe_allow_html=True)
    st.markdown("<p class='para'>Enter your query in below text area to classify the offense and retrieve related legal information.</p>", unsafe_allow_html=True)

    # Custom Styles for UI
    st.markdown(
        """
        <style>
        .header {
            text-align: center;
            padding: 20px;
        }
        .para {
            text-align: center;
        }
        .
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Custom CSS to adjust sidebar width, background color, and center Lottie animation
    st.markdown(
        """
        <style>
            /* Sidebar background color */
            .css-1d391kg { 
                background-color: #0E1117; 
            }

            /* Center the Lottie animation */
            .center {
                height: 100%;
            }
        </style>
        """, 
        unsafe_allow_html=True
    )


    # Function to load Lottie animation
    @st.cache_data
    def load_lottie_file(filepath: str):
        import json
        with open(filepath, "r") as f:
            return json.load(f)
        
    # Divide the page into two columns
    col1, col2 = st.columns([1, 2])

    # Sidebar with Lottie animation
    lottie_animation = load_lottie_file("assets/lottie.json")  # Replace with the actual Lottie file path
    with col1:
        st.markdown('<div class="center">', unsafe_allow_html=True)
        st_lottie.st_lottie(lottie_animation, speed=1, width=350, height=250, key="lottie")
        st.markdown('</div>', unsafe_allow_html=True)


    # Load environment variables
    load_dotenv()
    TOGETHER_AI_API = os.getenv("TOGETHER_AI")

    # Initialize Together API client
    client = Together(api_key=TOGETHER_AI_API)

    # Load FAISS database
    embeddings = HuggingFaceEmbeddings(
        model_name="nomic-ai/nomic-embed-text-v1",
        model_kwargs={"trust_remote_code": True, "revision": "289f532e14dbbbd5a04753fa58739e9ba766f3c7"}
    )
    db = FAISS.load_local("ipc_vector_db", embeddings, allow_dangerous_deserialization=True)
    db_retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    # Prompt Template
    prompt_template = """<s>[INST] You are an expert in the Indian Penal Code (IPC). 
    Your job is to classify the offense, identify relevant sections, and explain the punishment based on the provided query.

    QUERY: {query}

    Relevant Context:
    {context}

    Provide the output in the following format:
    - Predicted Offense: [Classified offense]
    - Relevant Legal Section: [Section details]
    - Punishment: [Punishment description]
    - Explanation: [Legal section explanation]
    </s>[INST]"""

    prompt = PromptTemplate(template=prompt_template, input_variables=["query", "context"])

    with col2:
        query = st.text_area("Enter your legal query:", height=160)  # height in pixels

        if st.button("Submit Query"):
            with st.spinner("Processing..."):
                try:
                    # Retrieve relevant documents from FAISS
                    context_docs = db_retriever.invoke(query)
                    context = " ".join([doc.page_content for doc in context_docs])
                    
                    # Format the prompt with query and context
                    formatted_prompt = prompt.format(query=query, context=context)

                    # Generate the response using Together API
                    response = client.chat.completions.create(
                        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
                        messages=[{"role": "user", "content": formatted_prompt}],
                        max_tokens=1024,
                        temperature=0.7,
                        top_p=0.7,
                        top_k=50,
                        repetition_penalty=1,
                        stop=["<|eot_id|>", "<|eom_id|>"],
                        stream=True
                    )

                    # Stream the response for better UX
                    final_response = ""
                    for token in response:
                        if hasattr(token, "choices"):
                            final_response += token.choices[0].delta.content
                            
                    time.sleep(1)  # Simulate slight delay for better UX

                    # Display the final response
                    st.success("Query processed successfully!")
                    st.markdown(f"### Query: {query}")
                    st.markdown(f"**Response:**\n{final_response}")

                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")