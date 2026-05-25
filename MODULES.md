# MODULES
## Overview
The project consists of several modules, each serving a specific purpose in the India Restaurant Finder application. This document provides an overview of the classes and functions in each module.

## app.py
### Functions
* `init_rag`: Initializes the RAG engine.

## prepare_data.py
### Functions
* `prepare_swiggy_data`: Cleans and filters the Swiggy dataset.
* `upload_to_google_sheets`: Uploads data to Google Sheets.

## rag_engine.py
### Classes
* `RAGEngine`: The RAG engine class, responsible for processing user queries.
	+ Methods:
		- `__init__`: Initializes the RAGEngine instance.
		- `_load_google_sheet_data`: Loads data from Google Sheets.
		- `_load_and_index_data`: Loads data from Google Sheets and creates a vector index.
		- `query`: Processes a user query with RAG.

## setup_azure_index.py
### Functions
* `create_search_index`: Creates an Azure Cognitive Search index with vector search capability.

## Module Interactions
The modules interact with each other to provide the functionality of the India Restaurant Finder application. The `prepare_data.py` module prepares the Swiggy dataset and uploads it to Google Sheets. The `rag_engine.py` module uses this data to process user queries. The `setup_azure_index.py` module creates an Azure Cognitive Search index for vector search capability. The `app.py` module initializes the RAG engine.