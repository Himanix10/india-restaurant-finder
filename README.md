# India Restaurants Finder
==========================

## Project Overview
The India Restaurants Finder is a Streamlit application designed to help users find restaurants in India. The application utilizes the RAG (Retrieval-Augmented Generator) engine, which is powered by Azure Cognitive Search and Sentence Transformers. The application also includes a data preparation script to clean and filter the Swiggy dataset.

## Architecture
The application consists of the following components:

* **app.py**: The main application file that renders the UI and handles user queries.
* **prepare_data.py**: A script that cleans and filters the Swiggy dataset.
* **rag_engine.py**: The RAG engine implementation that utilizes Azure Cognitive Search and Sentence Transformers.
* **setup_azure_index.py**: A script that creates an Azure Cognitive Search index with vector search capabilities.

## Tech Stack
The application uses the following technologies:

* **Streamlit**: A Python library for building web applications.
* **Azure Cognitive Search**: A cloud-based search service that provides vector search capabilities.
* **Sentence Transformers**: A library for sentence embeddings and semantic search.
* **Pandas**: A library for data manipulation and analysis.
* **Google Sheets API**: A library for interacting with Google Sheets.

## Setup Instructions
To set up the application, follow these steps:

### Step 1: Install Dependencies
Install the required dependencies by running the following command:
```bash
pip install streamlit pandas sentence-transformers azure-search-documents google-auth google-auth-oauthlib google-auth-httplib2
```

### Step 2: Set up Environment Variables
Create a `.env` file with the following environment variables:
```makefile
AZURE_SEARCH_KEY=
AZURE_SEARCH_NAME=
GOOGLE_CREDENTIALS=
SWIGGY_FILE=
CREDENTIALS_FILE=
SHEET_ID=
```
Replace the values with your own Azure Search key, Azure Search name, Google credentials, Swiggy file path, credentials file path, and sheet ID.

### Step 3: Prepare Data
Run the `prepare_data.py` script to clean and filter the Swiggy dataset:
```bash
python prepare_data.py
```

### Step 4: Set up Azure Index
Run the `setup_azure_index.py` script to create an Azure Cognitive Search index with vector search capabilities:
```bash
python setup_azure_index.py
```

### Step 5: Run the Application
Run the `app.py` script to start the Streamlit application:
```bash
streamlit run app.py
```

## TODO
The following tasks are pending:

* Create a TODO.md file (done)
* Edit `app.py` to safe RAG engine import with try/except
* Edit `app.py` to modify `init_rag()` to handle failures, return None if unavailable
* Edit `app.py` to move RAG init after core UI rendering (titles, sidebar)
* Edit `app.py` to add `rag=None` handling in query processing with demo response
* Edit `app.py` to enhance sidebar to indicate demo mode clearly
* Test: Run app with missing env vars/rag_engine to confirm UI loads in demo mode