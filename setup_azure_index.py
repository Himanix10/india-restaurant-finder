from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchableField,
    SearchField,
    VectorSearch,
    VectorSearchProfile,
    HnswAlgorithmConfiguration,
)
from azure.core.credentials import AzureKeyCredential
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_search_index():
    """Create Azure Cognitive Search index with vector search capability"""
    
    print("🚀 Creating Azure Search Index...")
    
    endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
    key = os.getenv("AZURE_SEARCH_KEY")
    
    if not endpoint or not key:
        print("❌ Error: Azure credentials not found in .env file")
        return
    
    print(f"📍 Endpoint: {endpoint}")
    
    # Create index client
    index_client = SearchIndexClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )
    
    # Define index schema
    fields = [
        SimpleField(name="id", type="Edm.String", key=True),
        SearchableField(name="content", type="Edm.String"),
        SearchableField(name="name", type="Edm.String"),
        SearchableField(name="city", type="Edm.String", filterable=True),
        SearchableField(name="category", type="Edm.String", filterable=True),
        SimpleField(name="rating", type="Edm.Double", filterable=True, sortable=True),
        SimpleField(name="phone", type="Edm.String"),
        SimpleField(name="area", type="Edm.String"),
        SimpleField(name="price", type="Edm.String"),
        SimpleField(name="maps_link", type="Edm.String"),
        SearchField(
            name="contentVector",
            type="Collection(Edm.Single)",
            searchable=True,
            vector_search_dimensions=384,  # all-MiniLM-L6-v2 embedding dimension
            vector_search_profile_name="vector-profile"
        ),
    ]
    
    # Vector search configuration
    vector_search = VectorSearch(
        profiles=[
            VectorSearchProfile(
                name="vector-profile",
                algorithm_configuration_name="hnsw-config"
            )
        ],
        algorithms=[
            HnswAlgorithmConfiguration(name="hnsw-config")
        ]
    )
    
    # Create index
    index = SearchIndex(
        name="india-services-index",
        fields=fields,
        vector_search=vector_search
    )
    
    try:
        result = index_client.create_or_update_index(index)
        print(f"✅ Index '{result.name}' created successfully!")
        print(f"📊 Total fields: {len(result.fields)}")
        print(f"🔍 Vector search enabled: Yes")
        print("\n🎉 Azure index is ready for data!")
        return True
    except Exception as e:
        print(f"❌ Error creating index: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("AZURE COGNITIVE SEARCH - INDEX SETUP")
    print("=" * 60)
    print()
    
    success = create_search_index()
    
    if success:
        print("\n✅ Setup complete! You can now proceed to build the chatbot.")
    else:
        print("\n❌ Setup failed. Please check your Azure credentials.")
    
    print("=" * 60)