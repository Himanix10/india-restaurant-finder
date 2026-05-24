# India Restaurants Finder
## Project Overview
India Restaurants Finder is a Streamlit application designed to help users find restaurants in India. The application utilizes a RAG (Retrieval-Augmented Generator) engine to provide accurate search results. The project consists of multiple components, including data preparation, RAG engine initialization, and a user-friendly interface.

## Architecture
The application architecture can be broken down into the following components:
* **Data Preparation**: The `prepare_data.py` script is responsible for cleaning and filtering the Swiggy dataset.
* **RAG Engine**: The `rag_engine.py` script initializes the RAG engine, which is used for searching and retrieving relevant data.
* **Azure Index Setup**: The `setup_azure_index.py` script sets up the Azure Cognitive Search index with vector search capabilities.
* **Streamlit Application**: The `app.py` script is the main entry point of the application, responsible for rendering the user interface and handling user queries.

## Tech Stack
The project utilizes the following technologies:
* **Streamlit**: A Python library for building web applications.
* **Azure Cognitive Search**: A cloud-based search service for indexing and querying data.
* **Groq**: A library for building and deploying machine learning models.
* **Sentence Transformers**: A library for sentence embeddings and semantic search.
* **Google Sheets API**: For interacting with Google Sheets.
* **Pandas**: A library for data manipulation and analysis.

## Setup Instructions
To set up the project, follow these steps:
1. **Install Dependencies**: Run `pip install -r requirements.txt` to install the required dependencies.
2. **Set Environment Variables**: Create a `.env` file and add the following environment variables:
	* `AZURE_SEARCH_KEY`
	* `AZURE_SEARCH_SERVICE_NAME`
	* `GOOGLE_CREDENTIALS_FILE`
	* `SWIGGY_FILE`
	* `SHEET_ID`
3. **Prepare Data**: Run `python prepare_data.py` to prepare the Swiggy dataset.
4. **Setup Azure Index**: Run `python setup_azure_index.py` to create the Azure Cognitive Search index.
5. **Run Application**: Run `streamlit run app.py` to start the Streamlit application.
6. **Test Application**: Open a web browser and navigate to `http://localhost:8501` to test the application.

## Troubleshooting
If you encounter any issues during setup or runtime, refer to the `TODO.md` file for a list of known tasks and potential solutions. Additionally, you can run `python test.py` to test the Streamlit application in a minimal configuration.