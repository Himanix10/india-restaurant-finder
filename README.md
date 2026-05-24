# India Restaurants Finder
## Project Overview
India Restaurants Finder is a Streamlit application designed to help users find restaurants in India. The application utilizes a RAG (Retrieval-Augmented Generator) engine, which is powered by Azure Cognitive Search and Sentence Transformers. The RAG engine enables the application to provide more accurate and relevant search results.

## Architecture
The application consists of the following components:

* `app.py`: The main application file, responsible for rendering the user interface and handling user input.
* `prepare_data.py`: A script used to clean and filter the Swiggy dataset.
* `rag_engine.py`: The RAG engine implementation, which utilizes Azure Cognitive Search and Sentence Transformers to provide search results.
* `setup_azure_index.py`: A script used to create an Azure Cognitive Search index with vector search capabilities.
* `test.py`: A test file used to verify that Streamlit is working correctly.

## Tech Stack
The application uses the following technologies:

* **Streamlit**: A Python library used to create the user interface.
* **Azure Cognitive Search**: A cloud-based search service used to power the RAG engine.
* **Sentence Transformers**: A library used to generate vector embeddings for search queries and documents.
* **Google Sheets**: Used to store and retrieve data.
* **OAuth 2.0**: Used to authenticate with Google Sheets.

## Setup Instructions
To set up the application, follow these steps:

1. **Install dependencies**: Run `pip install -r requirements.txt` to install the required dependencies.
2. **Create environment variables**: Create a `.env` file with the following variables:
	* `AZURE_SEARCH_KEY`: Your Azure Cognitive Search key.
	* `AZURE_SEARCH_NAME`: Your Azure Cognitive Search name.
	* `GOOGLE_CREDENTIALS`: The path to your Google credentials file.
	* `SWIGGY_FILE`: The path to the Swiggy dataset file.
3. **Create Azure Cognitive Search index**: Run `python setup_azure_index.py` to create an Azure Cognitive Search index with vector search capabilities.
4. **Prepare data**: Run `python prepare_data.py` to clean and filter the Swiggy dataset.
5. **Run the application**: Run `streamlit run app.py` to start the application.

## Running in Demo Mode
If the RAG engine is not available, the application will run in demo mode. In demo mode, the application will use a mock search response to simulate the RAG engine. To run the application in demo mode, simply start the application without setting up the RAG engine.

## TODO
The following tasks are still pending:

* Create a TODO.md file (done)
* Edit `app.py` to safely import the RAG engine with try/except
* Edit `app.py` to modify `init_rag()` to handle failures and return None if unavailable
* Edit `app.py` to move RAG init after core UI rendering (titles, sidebar)
* Edit `app.py` to add `rag=None` handling in query processing with demo response
* Edit `app.py` to enhance the sidebar to indicate demo mode clearly
* Test: Run the application with missing environment variables/rag_engine to confirm the UI loads in demo mode