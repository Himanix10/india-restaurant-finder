# Project Overview
The India Restaurants Finder is a Streamlit application designed to help users find restaurants in India. The application utilizes a RAG (Retrieval-Augmented Generator) engine to provide accurate and relevant search results. The project consists of multiple components, including data preparation, RAG engine initialization, and a Streamlit interface.

## Architecture
The project architecture can be broken down into the following components:
* **Data Preparation**: The `prepare_data.py` script is responsible for cleaning and filtering the Swiggy dataset.
* **RAG Engine**: The `rag_engine.py` script initializes the RAG engine, which is used to generate search results.
* **Streamlit Interface**: The `app.py` script creates the Streamlit interface, which allows users to interact with the application.
* **Azure Index Setup**: The `setup_azure_index.py` script sets up the Azure Cognitive Search index with vector search capabilities.

## Tech Stack
The project utilizes the following technologies:
* **Streamlit**: A Python library for creating web applications.
* **RAG Engine**: A retrieval-augmented generator engine for generating search results.
* **Azure Cognitive Search**: A cloud-based search service for indexing and searching data.
* **Google Sheets**: A cloud-based spreadsheet service for storing and retrieving data.
* **Pandas**: A Python library for data manipulation and analysis.
* **Sentence Transformers**: A Python library for sentence embeddings and semantic search.

## Setup Instructions
To set up the project, follow these steps:
1. **Install Dependencies**: Install the required dependencies by running `pip install -r requirements.txt`.
2. **Set Environment Variables**: Set the environment variables in the `.env` file, including `AZURE_SEARCH_KEY`, `AZURE_SEARCH_NAME`, and `GOOGLE_CREDENTIALS`.
3. **Prepare Data**: Run the `prepare_data.py` script to clean and filter the Swiggy dataset.
4. **Setup Azure Index**: Run the `setup_azure_index.py` script to create the Azure Cognitive Search index.
5. **Initialize RAG Engine**: Run the `rag_engine.py` script to initialize the RAG engine.
6. **Run Streamlit App**: Run the `app.py` script to start the Streamlit application.

## Running the Application
To run the application, navigate to the project directory and run `streamlit run app.py`. This will start the Streamlit application, and you can interact with it by visiting `http://localhost:8501` in your web browser.

## Testing
To test the application, run the `test.py` script. This will start a simple Streamlit application that tests the Streamlit installation.

## TODO
For a list of tasks to be completed, refer to the `TODO.md` file. This file outlines the tasks that need to be completed to refactor the Streamlit application and improve its functionality.