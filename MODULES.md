# MODULES
## Overview
The India Restaurant Finder application consists of several modules, each responsible for a specific functionality. This document provides an overview of the purpose and functionality of each module.

## app.py
### Purpose
The `app.py` module is the main entry point of the application. It contains a single function, `init_rag`, which is used to initialize the RAG engine.

### Functions
* `init_rag`: Initializes the RAG engine.

## prepare_data.py
### Purpose
The `prepare_data.py` module is responsible for preparing and uploading data to Google Sheets. It contains two functions: `prepare_swiggy_data` and `upload_to_google_sheets`.

### Functions
* `prepare_swiggy_data`: Cleans and filters the Swiggy dataset.
* `upload_to_google_sheets`: Uploads data to Google Sheets.

## rag_engine.py
### Purpose
The `rag_engine.py` module contains the `RAGEngine` class, which is responsible for processing user queries with RAG. It also contains several functions for loading and indexing data.

### Classes
* `RAGEngine`: The RAG engine class.
	+ Methods:
		- `__init__`: Initializes the RAG engine.
		- `_load_google_sheet_data`: Loads data from Google Sheets.
		- `_load_and_index_data`: Loads data from Google Sheets and creates a vector index.
		- `query`: Processes a user query with RAG.

### Functions
* `__init__`: Initializes the RAG engine.
* `_load_google_sheet_data`: Loads data from Google Sheets.
* `_load_and_index_data`: Loads data from Google Sheets and creates a vector index.
* `query`: Processes a user query with RAG.

## setup_azure_index.py
### Purpose
The `setup_azure_index.py` module is responsible for creating an Azure Cognitive Search index with vector search capability.

### Functions
* `create_search_index`: Creates an Azure Cognitive Search index with vector search capability.

## test.py
### Purpose
The `test.py` module is used for testing the application. It does not contain any functions or classes.

### Note
The `test.py` module is currently empty and does not contain any functionality.