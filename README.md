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
- **FAISS**: A vector database to store and search for relevant legal data (both from `.csv` and `.pdf` files) using similarity search.
- **Hugging Face Embeddings**: For converting the legal dataset into embeddings.
- **Together AI**: For integrating **LLAMA 3.3**, an LLM that processes user queries and returns answers based on context.
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

## Installation

### Prerequisites
- Python 3.x
- Streamlit
- Hugging Face Embeddings
- FAISS

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/katakampranav/LegalQ.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file to store your **API token** (from Together AI):
   ```plaintext
   API_TOKEN=your_api_token_here
   ```

### Running the Application
1. Start Streamlit:
   ```bash
   streamlit run app.py
   ```
2. Access the app through your browser, where you can interact with the **Need Info** or **Know Law** functionality.

## Example Usage

- **Need Info**: Select an offense and its relevant legal section from dropdowns to get detailed legal information.
- **Know Law**: Enter a query (e.g., "A person stabbed B in self-defense"), and the system will generate a detailed response with the relevant legal sections, offense, punishment, and explanation.

## Author

This LegalQ application was developed by :
-	[@katakampranav](https://github.com/katakampranav)
-	Repository : https://github.com/katakampranav/LegalQ

---
