# Project Overview
India Restaurants Finder is a Streamlit application designed to help users find restaurants in India. The application utilizes a RAG (Retrieval-Augmented Generator) engine to provide accurate search results. The project consists of multiple components, including data preparation, RAG engine initialization, and a Streamlit interface.

## Architecture
The application architecture is divided into the following components:
* **Data Preparation**: The `prepare_data.py` script is responsible for cleaning and filtering the Swiggy dataset.
* **RAG Engine**: The `rag_engine.py` script initializes the RAG engine, which is used for searching and retrieving relevant data.
* **Streamlit Interface**: The `app.py` script sets up the Streamlit interface, including page configuration, custom CSS, and query processing.
* **Azure Index Setup**: The `setup_azure_index.py` script creates an Azure Cognitive Search index with vector search capabilities.

## Tech Stack
The project utilizes the following technologies:
* **Streamlit**: A Python library for building web applications.
* **RAG Engine**: A retrieval-augmented generator engine for searching and retrieving data.
* **Azure Cognitive Search**: A cloud-based search service for indexing and querying data.
* **Google Sheets**: A cloud-based spreadsheet service for storing and retrieving data.
* **Pandas**: A Python library for data manipulation and analysis.
* **Sentence Transformers**: A Python library for sentence embeddings and semantic search.

## Setup Instructions
To set up the project, follow these steps:
1. **Install Dependencies**: Install the required dependencies, including Streamlit, Pandas, and Sentence Transformers.
2. **Set up Environment Variables**: Set up environment variables for Azure Cognitive Search and Google Sheets.
3. **Prepare Data**: Run the `prepare_data.py` script to clean and filter the Swiggy dataset.
4. **Initialize RAG Engine**: Run the `rag_engine.py` script to initialize the RAG engine.
5. **Create Azure Index**: Run the `setup_azure_index.py` script to create an Azure Cognitive Search index.
6. **Run Streamlit App**: Run the `app.py` script to start the Streamlit application.

## Testing
To test the application, run the `test.py` script to verify that Streamlit is working correctly. Additionally, test the application with missing environment variables or a unavailable RAG engine to confirm that the UI loads in demo mode.

## TODO
Refer to the `TODO.md` file for a list of tasks to be completed, including refactoring the Streamlit app, editing the `app.py` script, and testing the application.