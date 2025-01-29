# LegalQ

LegalQ is an AI-powered application built using **Streamlit** that helps users retrieve legal sections, offenses, punishments, and their explanations based on their queries. It is designed to streamline access to legal knowledge and provide intelligent responses based on input from the user.

## Workflow Overview

The application consists of two main functionalities:
1. **Need Info**: For users who know the offense and the corresponding legal section. The user selects the offense and legal section from dropdown menus and submits the query to receive relevant legal sections, offenses, punishments, and explanations.
2. **Know Law**: For users who have a legal question or query, like "A person stabbed B in self-defense." The system processes the query and generates legal predictions based on the context provided.

## How It Works

- The system processes and stores data from the **IPC dataset** (in both `.pdf` and `.csv` formats).
- The text from these documents is parsed and converted into **vector embeddings** using **Hugging Face** embeddings, which are then stored in the **FAISS** vector database.
- The query submitted by the user is passed to FAISS, where it performs **similarity search** to find relevant content based on the embeddings.
- The relevant context is dynamically passed to a **Large Language Model (LLM)** using the **Together AI** platform (with **LLAMA 3.3** model) via an API call. The LLM generates predictions based on the retrieved context.

### Components and Libraries Used:

- **Streamlit**: Used for creating the user interface.
- **FAISS**: A vector database to store the given data(both from `.csv` and `.pdf` files) in the form of embeddings and search for relevant legal data using similarity search while generating output.
- **Hugging Face Embeddings**: For converting the legal datasets into embeddings.
- **Together AI**: For integrating [**LLAMA 3.3**](https://api.together.xyz/models/meta-llama/Llama-3.3-70B-Instruct-Turbo-Free), an LLM that processes user queries and returns answers based on context.
- **Langchain**: Used for various utilities such as document loaders, text splitting, and vector stores.
- **dotenv**: For securely loading API tokens from environment files.

## Technical Workflow

1. **Document Parsing & Embedding**:
   - Legal content from `ipc-data.pdf` and `ipc-dataset.csv` is parsed using the **PyPDFLoader** and loaded into a **DataFrame** using **Pandas**.
   - The text is split using **RecursiveCharacterTextSplitter** and then converted into **embeddings** using **Hugging Face Embeddings**.
   
2. **FAISS Vectorstore**:
   - The embeddings are stored in the **FAISS vector database**, which facilitates efficient **similarity searches**.
   
3. **Query Processing**:
   - When a user submits a query, the system performs a similarity search in FAISS, retrieves relevant context, and dynamically forms a prompt for the **LLAMA 3.3** model using the **Langchain** prompt template.
   - The **Together AI API** sends the prompt to **LLAMA 3.3**, which generates predictions, including:
     - Legal Sections
     - Offenses
     - Punishments
     - Legal Section Explanations

## Features

- **Legal Information Retrieval**: Get detailed responses about legal sections, offenses, punishments, and explanations.
- **Contextual Query Processing**: Dynamic context generation based on the user's query.
- **Intelligent Answering System**: Powered by **LLAMA 3.3**, offering AI-driven responses based on the relevant legal data.

## Tech Stack

- **Streamlit**: Web interface for the app.
- **Langchain**: For managing documents, prompts, and vectorstores (FAISS).
- **FAISS**: For storing and retrieving legal data based on vector similarity search.
- **Together AI (LLAMA 3.3)**: LLM model for generating predictions based on context.
- **Hugging Face Embeddings**: For generating text embeddings.
- **Pandas**: For handling and manipulating data.

## Workflow
![Image](https://github.com/user-attachments/assets/0b201efc-693b-4d71-96c8-7e7338d1eced)

## Installation

### Prerequisites
- Python 3.x
- Streamlit
- Hugging Face Embeddings
- FAISS
- Langchain

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/katakampranav/LegalQ.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Go to Model_Development Directory:
   ```bash
   cd Model_Development
   ```

5. Create a `.env` file to store your **API token** (from Together AI):
   ```plaintext
   TOGETHER_AI=your_api_token_here
   ```

### Running the Application
1. Start Streamlit:
   ```bash
   streamlit run app.py
   ```
2. Access the app through your browser, where you can interact with the **Need Info** or **Know Law** functionality.

## Example Usage
- **Home Page**:
  ![Image](https://github.com/user-attachments/assets/ad17ada9-5880-45c8-85a6-93420a0f40bb)
- **Need Info**: Select an offense and its relevant legal section from dropdowns to get detailed legal information.
  ![Image](https://github.com/user-attachments/assets/25a29832-589d-4c11-9010-7c21aca1b5a8)

  ![Image](https://github.com/user-attachments/assets/74a50f08-8c57-4567-b910-a29d597772fc)
  ![Image](https://github.com/user-attachments/assets/f369a523-88f3-418f-9d79-ddf73756d27e)
- **Know Law**: Enter a query (e.g., "A person stabbed B in self-defense"), and the system will generate a detailed response with the relevant legal sections, offense, punishment, and explanation.
  ![Image](https://github.com/user-attachments/assets/5b14f9f7-292e-4845-845c-e27560d39b38)

  ![Image](https://github.com/user-attachments/assets/1dbcf61c-a80c-4075-a5ce-8ed7559f0c67)
  
## Author

This LegalQ application was developed by :
-	[@katakampranav](https://github.com/katakampranav)
-	Repository : https://github.com/katakampranav/LegalQ

## Feedback

For any feedback or queries, please reach out to me at katakampranavshankar@gmail.com.

---
