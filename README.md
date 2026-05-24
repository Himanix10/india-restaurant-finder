# Project Overview
The India Restaurants Finder is a Streamlit application designed to help users find restaurants in India. The application utilizes a RAG (Retrieval-Augmented Generator) engine to provide accurate and relevant search results. The project consists of multiple components, including data preparation, RAG engine initialization, and a user-friendly interface.

## Architecture
The application's architecture can be broken down into the following components:
* **Data Preparation**: The `prepare_data.py` script is responsible for cleaning and filtering the Swiggy dataset, which is used to train the RAG engine.
* **RAG Engine**: The `rag_engine.py` script initializes the RAG engine, which is used to generate search results. The engine utilizes the Groq library, Azure Cognitive Search, and Sentence Transformers.
* **Streamlit Application**: The `app.py` script is the main entry point of the application, responsible for rendering the user interface and handling user input.
* **Azure Index Setup**: The `setup_azure_index.py` script is used to create an Azure Cognitive Search index with vector search capabilities.

## Tech Stack
The project utilizes the following technologies:
* **Streamlit**: A Python library for building web applications
* **Groq**: A library for building and deploying machine learning models
* **Azure Cognitive Search**: A cloud-based search service for building search indexes
* **Sentence Transformers**: A library for generating sentence embeddings
* **Google OAuth**: A library for authenticating with Google services
* **Azure Key Credential**: A library for authenticating with Azure services

## Setup Instructions
To set up the application, follow these steps:
1. **Install dependencies**: Run `pip install -r requirements.txt` to install the required dependencies.
2. **Set environment variables**: Create a `.env` file and add the following environment variables:
	* `AZURE_SEARCH_KEY`
	* `AZURE_SEARCH_SERVICE_NAME`
	* `GOOGLE_CREDENTIALS_FILE`
	* `SWIGGY_FILE`
	* `SHEET_ID`
3. **Prepare data**: Run `python prepare_data.py` to prepare the Swiggy dataset.
4. **Create Azure index**: Run `python setup_azure_index.py` to create an Azure Cognitive Search index.
5. **Run the application**: Run `streamlit run app.py` to start the application.

## Testing
To test the application, run `python test.py` to verify that Streamlit is working correctly. You can also test the application by running it with missing environment variables or a non-functional RAG engine to confirm that the UI loads in demo mode.

## TODO
The following tasks are still pending:
* Create TODO.md (done)
* Edit `app.py`: Safe RAGEngine import with try/except
* Edit `app.py`: Modify `init_rag()` to handle failures, return None if unavailable
* Edit `app.py`: Move RAG init after core UI rendering (titles, sidebar)
* Edit `app.py`: Add `rag=None` handling in query processing with demo response
* Edit `app.py`: Enhance sidebar to indicate demo mode clearly
* Test: Run app with missing env vars/rag_engine to confirm UI loads in demo mode