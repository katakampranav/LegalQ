from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from together import Together
import os
import streamlit as st
import time
import streamlit_lottie as st_lottie  # For Lottie file integration

def render_page():

    # Load environment variables
    load_dotenv()
    TOGETHER_AI_API = os.getenv("TOGETHER_AI")

    # Initialize Together API client
    client = Together(api_key=TOGETHER_AI_API)

    # Custom Styles for UI
    st.markdown(
        """
        <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
        }
        .header {
            text-align: center;
            padding: 20px;
        }
        .input-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-bottom: 20px;
        }
        .input-container select,
        .input-container input {
            padding: 10px;
            margin: 10px;
            width: 70%;
            border-radius: 10px;
            border: 1px solid #ddd;
            font-size: 16px;
        }
        .para {
            text-align: center;
        }
        .
        </style>
        """,
        unsafe_allow_html=True,
    )

    offense_section_mapping = {
        "Choose an offense": "Choose a legal section",
        "murder": "Section 302",
        "theft": "Section 379",
        "fraud": "Section 420",
        "assault": "Section 351",
        "robbery": "Section 392",
        "rape": "Section 375",
        "homicide": "Section 299",
        "arson": "Section 435",
        "kidnapping": "Section 359",
        "bribery": "Section 171E",
        "embezzlement": "Section 403",
        "extortion": "Section 383",
        "trespassing": "Section 441",
        "smuggling": "Section 135 (Customs Act, not IPC)",
        "perjury": "Section 191",
        "forgery": "Section 463",
        "manslaughter": "Section 304",
        "cheating": "Section 415",
        "corruption": "Section 171B",
        "defamation": "Section 499",
        "wearing the dress of a soldier": "Section 140",
        "carrying a token of a soldier": "Section 140",
        "impersonating a soldier": "Section 171",
        "false representation": "Section 82",
        "misleading identity": "Section 416",
        "adultery": "Section 497 (Note: Decriminalized in 2018)",
        "bigamy": "Section 494",
        "criminal conspiracy": "Section 120B",
        "public mischief": "Section 505",
        "obscenity": "Section 294",
        "hate speech": "Section 153A",
        "sedition": "Section 124A",
        "terrorism": "Section 15 (Unlawful Activities Prevention Act, not IPC)",
        "unlawful assembly": "Section 141",
        "criminal intimidation": "Section 503",
        "criminal breach of trust": "Section 405",
        "death threats": "Section 506",
        "causing hurt": "Section 319",
        "grievous hurt": "Section 320",
        "abduction": "Section 362",
        "stalking": "Section 354D",
        "voyeurism": "Section 354C",
        "insult": "Section 504",
        "offensive conduct": "Section 509",
        "dishonest misappropriation": "Section 403",
        "criminal negligence": "Section 304A",
        "outraging modesty": "Section 354",
        "rioting": "Section 146",
        "dacoity": "Section 391",
        "dangerous driving": "Section 279",
        "culpable homicide": "Section 299",
        "disobedience to orders of public servants": "Section 188",
        "affray": "Section 159",
        "negligent conduct": "Section 336",
        "illegal detention": "Section 340",
        "corrupt practices": "Section 171G",
        "vandalism": "Section 427",
        "incitement": "Section 153",
        "enticement": "Section 361",
        "injury to reputation": "Section 499",
        "criminal act by public servant": "Section 166",
        "abandonment": "Section 317",
        "blasphemy": "Section 295A",
        "fraudulent bankruptcy": "Section 421",
        "false evidence": "Section 191",
        "impersonation": "Section 416",
        "criminal contempt": "Contempt of Courts Act, 1971",
        "disruption of public peace": "Section 268",
        "child abuse": "Section 75 (Juvenile Justice Act)",
        "cybercrime": "Section 66 (IT Act, not IPC)",
        "money laundering": "Prevention of Money Laundering Act",
        "hate crime": "Section 153A",
        "brutality": "Section 326",
        "racial discrimination": "Section 153A",
        "child labor": "Child Labour (Prohibition and Regulation) Act",
        "attempt to murder": "Section 307",
        "sexual harassment": "Section 354A",
        "exploitation": "Section 370",
        "gang-rape": "Section 376D",
        "unlawful confinement": "Section 340",
        "public nuisance": "Section 268",
        "selling narcotics": "Narcotic Drugs and Psychotropic Substances Act",
        "illegal drugs": "Narcotic Drugs and Psychotropic Substances Act",
        "human trafficking": "Section 370",
        "animal cruelty": "Prevention of Cruelty to Animals Act",
        "prostitution": "Immoral Traffic (Prevention) Act",
        "blackmail": "Section 503",
        "child pornography": "Section 67B (IT Act, not IPC)",
        "hunting protected species": "Wildlife Protection Act",
        "destruction of public property": "Section 3 (Prevention of Damage to Public Property Act)",
        "impersonating a police officer": "Section 170",
        "organ trafficking": "Transplantation of Human Organs Act",
        "match-fixing": "Section 420",
        "misuse of public office": "Prevention of Corruption Act",
        "insider trading": "SEBI Act",
        "spreading false rumors": "Section 505",
        "defamation of religion": "Section 295A",
        "illegal mining": "Mines and Minerals (Regulation and Development) Act",
        "violence against women": "Section 498A",
        "violation of privacy": "Section 354D",
        "contamination of food": "Section 272",
        "embezzlement by public servant": "Section 409",
        "illegal arms trade": "Arms Act",
        "riot causing death": "Section 147",
        "pollution": "Environment Protection Act",
        "cyberbullying": "Section 66 (IT Act)",
        "illegal hunting": "Wildlife Protection Act",
        "extortion of confidential information": "Section 383",
        "illegal immigration": "Passport Act",
        "disobeying court orders": "Section 188",
        "illegal collection of data": "IT Act",
        "demanding ransom": "Section 364A",
        "theft of intellectual property": "Copyright Act",
        "cyberstalking": "Section 354D",
        "forgery of currency": "Section 489A",
        "abusing a position of power": "Section 166",
        "false imprisonment": "Section 340",
        "fraudulent marriage": "Section 493",
        "leaking state secrets": "Official Secrets Act",
        "financial fraud": "Section 420",
        "luring minors": "Section 361",
        "counterfeiting": "Section 489A",
        "violence against animals": "Prevention of Cruelty to Animals Act",
        "false medical certificates": "Section 197",
        "hacking": "Section 66 (IT Act)",
        "damaging private property": "Section 427",
        "public intoxication": "Section 268",
        "offensive behavior": "Section 294",
        "disrupting religious gatherings": "Section 295",
        "treason": "Section 121",
        "exposing state secrets": "Official Secrets Act",
        "illegal surveillance": "IT Act",
        "theft of personal data": "IT Act",
        "identity theft": "Section 66C (IT Act)",
        "stolen property": "Section 411",
        "fraudulent representation": "Section 420",
        "cultural vandalism": "Section 295"
    }

    Offenses, Sections = zip(*offense_section_mapping.items())
    Offenses = list(Offenses)
    Sections = list(Sections)

    # Function to load Lottie animation
    @st.cache_data
    def load_lottie_file(filepath: str):
        import json
        with open(filepath, "r") as f:
            return json.load(f)

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

    # Streamlit Title
    st.markdown("<h1 class='header'>LegalQ</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='header'>A Legal Offense Query System</h3>", unsafe_allow_html=True)
    st.markdown("<p class='para'>Choose the offence and relevant legal section from dropdowns provided below to classify the offense and retrieve related legal information.</p>", unsafe_allow_html=True)

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

    # Divide the page into two columns
    col1, col2 = st.columns([1, 2])

    # Sidebar with Lottie animation
    lottie_animation = load_lottie_file("assets/lottie.json")  # Replace with the actual Lottie file path
    with col1:
        st.markdown('<div class="center">', unsafe_allow_html=True)
        st_lottie.st_lottie(lottie_animation, speed=1, width=350, height=250, key="lottie")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # Input section with dropdowns and placeholders
        st.markdown("<div class='input-container'>", unsafe_allow_html=True)

        # Dropdown for selecting common offenses
        offenses = Offenses
        selected_offense = st.selectbox("Select an offense:", offenses)

        # Dropdown for legal sections
        sections = Sections
        selected_section = st.selectbox("Select a legal section:", sections)

        # Text input for query
        query = f"Offense: {selected_offense}, Section: {selected_section}"

        st.markdown("</div>", unsafe_allow_html=True)

        # Submit Query button
        if st.button("Submit Query"):
            if selected_offense == "Choose an offense" or selected_section == "Choose a legal section":
                st.error("Please select both an offense and a legal section before submitting.")
            else:
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

                        # Display results
                        st.success("Query processed successfully!")
                        st.markdown(f"### Query: {query}")

                        # Display response
                        st.markdown(f"**Predictions:**\n{final_response}")
                        st.markdown("</div>", unsafe_allow_html=True)

                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")