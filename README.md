# India Restaurants Finder
==========================

## Project Overview
The India Restaurants Finder is a Streamlit application designed to help users find restaurants in India. The application utilizes a RAG (Retrieval-Augmented Generator) engine to provide accurate search results. The project consists of multiple components, including data preparation, RAG engine initialization, and a user-friendly interface.

## Architecture
The application architecture can be broken down into the following components:

* **Data Preparation**: The `prepare_data.py` script is responsible for cleaning and filtering the Swiggy dataset.
* **RAG Engine**: The `rag_engine.py` script initializes the RAG engine, which is used to generate search results.
* **Azure Index Setup**: The `setup_azure_index.py` script creates an Azure Cognitive Search index with vector search capabilities.
* **Streamlit Application**: The `app.py` script is the main entry point of the application, responsible for rendering the user interface and handling user queries.

## Tech Stack
The project utilizes the following technologies:

* **Streamlit**: A Python library for building web applications.
* **Azure Cognitive Search**: A cloud-based search service for building search indexes.
* **Groq**: A library for building and deploying machine learning models.
* **Sentence Transformers**: A library for generating sentence embeddings.
* **Google Sheets API**: A library for interacting with Google Sheets.
* **Pandas**: A library for data manipulation and analysis.

## Setup Instructions
To set up the application, follow these steps:

### Step 1: Install Dependencies
Install the required dependencies by running the following command:
```bash
pip install streamlit pandas gspread google-auth sentence-transformers groq azure-search-documents
```
### Step 2: Set Environment Variables
Create a `.env` file and add the following environment variables:
```makefile
AZURE_SEARCH_KEY=
AZURE_SEARCH_SERVICE_NAME=
GOOGLE_SHEETS_CREDENTIALS=
SWIGGY_FILE=
CREDENTIALS_FILE=
SHEET_ID=
```
Replace the placeholders with your actual Azure Search key, service name, Google Sheets credentials, Swiggy file path, credentials file path, and sheet ID.

### Step 3: Prepare Data
Run the `prepare_data.py` script to prepare the Swiggy dataset:
```bash
python prepare_data.py
```
### Step 4: Set up Azure Index
Run the `setup_azure_index.py` script to create an Azure Cognitive Search index:
```bash
python setup_azure_index.py
```
### Step 5: Run the Application
Run the `app.py` script to start the Streamlit application:
```bash
streamlit run app.py
```
Open a web browser and navigate to `http://localhost:8501` to access the application.

## Troubleshooting
If you encounter any issues during setup or runtime, refer to the `TODO.md` file for a list of known issues and potential solutions.