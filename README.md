# India Restaurants Finder
## Project Overview
India Restaurants Finder is a Streamlit application designed to help users find restaurants in India. The application utilizes a RAG (Retrieval-Augmented Generator) engine, which is powered by Azure Cognitive Search and Sentence Transformers. The RAG engine enables the application to provide more accurate and relevant search results.

## Architecture
The application consists of the following components:
* `app.py`: The main application file, responsible for initializing the RAG engine and providing a user interface for searching restaurants.
* `prepare_data.py`: A module used to clean and filter the Swiggy dataset, which is used to train the RAG engine.
* `rag_engine.py`: A module that implements the RAG engine, utilizing Azure Cognitive Search and Sentence Transformers to provide accurate search results.
* `setup_azure_index.py`: A script used to create an Azure Cognitive Search index with vector search capabilities.

## Tech Stack
The application is built using the following technologies:
* **Streamlit**: A Python library used to create the user interface and provide an interactive experience for users.
* **Azure Cognitive Search**: A cloud-based search service used to power the RAG engine and provide accurate search results.
* **Sentence Transformers**: A library used to generate vector embeddings for text data, which is used to improve the accuracy of search results.
* **Pandas**: A library used for data manipulation and analysis.
* **GSpread**: A library used to interact with Google Sheets.

## Setup Instructions
To set up the application, follow these steps:
1. **Install dependencies**: Run `pip install -r requirements.txt` to install the required dependencies.
2. **Create Azure Cognitive Search index**: Run `python setup_azure_index.py` to create an Azure Cognitive Search index with vector search capabilities.
3. **Prepare data**: Run `python prepare_data.py` to clean and filter the Swiggy dataset.
4. **Initialize RAG engine**: Run `python app.py` to initialize the RAG engine and start the application.
5. **Configure environment variables**: Set the following environment variables:
	* `AZURE_SEARCH_KEY`: The key to your Azure Cognitive Search service.
	* `AZURE_SEARCH_NAME`: The name of your Azure Cognitive Search service.
	* `GOOGLE_SHEETS_CREDENTIALS`: The path to your Google Sheets credentials file.
6. **Start the application**: Run `streamlit run app.py` to start the application.

## Modules
For more information about the individual modules, see [MODULES.md](MODULES.md).

## Contributing
To contribute to the project, please submit a pull request with your changes. Make sure to follow the standard professional guidelines for commit messages and code formatting.

## License
The project is licensed under the [MIT License](LICENSE).