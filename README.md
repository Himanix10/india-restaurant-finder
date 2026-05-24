# Project Overview
The India Restaurants Finder is a Streamlit application designed to help users find restaurants in India. The application utilizes a RAG (Retrieval-Augmented Generator) engine to provide accurate search results. The project consists of multiple components, including data preparation, RAG engine initialization, and a Streamlit interface.

## Architecture
The application architecture can be broken down into the following components:
* **Data Preparation**: The `prepare_data.py` script is responsible for cleaning and filtering the Swiggy dataset.
* **RAG Engine**: The `rag_engine.py` script initializes the RAG engine, which is used for searching and retrieving relevant data.
* **Streamlit Interface**: The `app.py` script creates the Streamlit interface, which includes a page config, custom CSS, and a query processing system.
* **Azure Index Setup**: The `setup_azure_index.py` script sets up the Azure Cognitive Search index with vector search capabilities.

## Tech Stack
The project utilizes the following technologies:
* **Streamlit**: A Python library for creating web applications.
* **RAG Engine**: A retrieval-augmented generator engine for searching and retrieving data.
* **Azure Cognitive Search**: A cloud-based search service for indexing and querying data.
* **Google Sheets**: A cloud-based spreadsheet service for storing and retrieving data.
* **Pandas**: A Python library for data manipulation and analysis.
* **Sentence Transformers**: A Python library for sentence embeddings and semantic search.

## Setup Instructions
To set up the project, follow these steps:
1. **Install Dependencies**: Install the required dependencies, including Streamlit, Pandas, and Sentence Transformers.
2. **Set up Environment Variables**: Set up the environment variables, including the Azure key credential and Google Sheets credentials.
3. **Prepare Data**: Run the `prepare_data.py` script to clean and filter the Swiggy dataset.
4. **Set up Azure Index**: Run the `setup_azure_index.py` script to set up the Azure Cognitive Search index.
5. **Initialize RAG Engine**: Run the `rag_engine.py` script to initialize the RAG engine.
6. **Start Streamlit Application**: Run the `app.py` script to start the Streamlit application.

## Testing
To test the application, follow these steps:
1. **Run Test Script**: Run the `test.py` script to test the Streamlit application.
2. **Verify UI**: Verify that the UI loads correctly and displays the expected content.
3. **Test Query Processing**: Test the query processing system to ensure it returns accurate results.

## TODO
The following tasks are pending:
* Create TODO.md (done)
* Edit app.py: Safe RAGEngine import with try/except
* Edit app.py: Modify init_rag() to handle failures, return None if unavailable
* Edit app.py: Move RAG init after core UI rendering (titles, sidebar)
* Edit app.py: Add rag=None handling in query processing with demo response
* Edit app.py: Enhance sidebar to indicate demo mode clearly
* Test: Run app with missing env vars/rag_engine to confirm UI loads in demo mode