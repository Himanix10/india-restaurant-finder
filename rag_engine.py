from groq import Groq
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from azure.core.credentials import AzureKeyCredential
from sentence_transformers import SentenceTransformer
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv

load_dotenv()

class RAGEngine:
    def __init__(self):
        print("🚀 Initializing RAG Engine...")
        
        # Initialize Groq client
        self.groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        print("✅ Groq LLM connected")
        
        # Initialize Azure Search client
        endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
        key = os.getenv("AZURE_SEARCH_KEY")
        
        self.search_client = SearchClient(
            endpoint=endpoint,
            index_name="india-services-index",
            credential=AzureKeyCredential(key)
        )
        print("✅ Azure Search connected")
        
        # Initialize embedding model
        print("📦 Loading embedding model (this may take a minute)...")
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        print("✅ Embedding model loaded")
        
        # Load and index data
        self._load_and_index_data()
        print("✅ RAG Engine ready!")
    
    def _load_google_sheet_data(self):
        """Load data from Google Sheets"""
        print("📊 Loading data from Google Sheets...")
        
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            os.getenv('GOOGLE_CREDENTIALS_PATH'), 
            scope
        )
        
        client = gspread.authorize(creds)
        sheet_id = os.getenv('GOOGLE_SHEET_ID')
        sheet = client.open_by_key(sheet_id).sheet1
        
        data = sheet.get_all_records()
        df = pd.DataFrame(data)
        
        print(f"✅ Loaded {len(df)} records from Google Sheets")
        return df
    
    def _load_and_index_data(self):
        """Load from Google Sheets and create vector index"""
        data = self._load_google_sheet_data()
        
        if data.empty:
            print("⚠️ No data found in Google Sheets!")
            return
        
        print(f"🔄 Creating embeddings for {len(data)} entries...")
        
        documents = []
        for idx, row in data.iterrows():
            # Create searchable text
            text = (
                f"{row['Name']} is a {row['Category']} located in {row['Area']}, {row['City']}. "
                f"{row['Description']} "
                f"Rating: {row['Rating']}/5. "
                f"Price Range: {row['Price']}."
            )
            
            if row['Phone'] and row['Phone'] != 'N/A':
                text += f" Contact: {row['Phone']}"
            
            # Generate embedding
            embedding = self.embedder.encode(text).tolist()
            
            # Create document
            doc = {
                "id": f"doc_{idx}",
                "content": text,
                "contentVector": embedding,
                "city": str(row['City']),
                "category": str(row['Category']),
                "name": str(row['Name']),
                "rating": float(row['Rating']) if row['Rating'] else 4.0,
                "phone": str(row['Phone']) if row['Phone'] else 'N/A',
                "area": str(row['Area']),
                "price": str(row['Price']),
                "maps_link": str(row.get('Google_Maps_Link', ''))
            }
            documents.append(doc)
        
        # Upload to Azure Search
        try:
            print("☁️ Uploading to Azure Cognitive Search...")
            self.search_client.upload_documents(documents=documents)
            print(f"✅ Successfully indexed {len(documents)} documents")
        except Exception as e:
            print(f"❌ Indexing error: {e}")
    
    def query(self, user_query: str) -> str:
        """Process user query with RAG"""
        
        # Generate query embedding
        query_vector = self.embedder.encode(user_query).tolist()
        
        # Create vectorized query object
        vector_query = VectorizedQuery(
            vector=query_vector,
            k_nearest_neighbors=5,
            fields="contentVector"
        )
        
        # Search Azure with hybrid search (keyword + vector)
        try:
            results = self.search_client.search(
                search_text=user_query,
                vector_queries=[vector_query],
                select=["name", "content", "city", "rating", "phone", "area", "price"],
                top=5
            )
            
            # Build context from results
            context_parts = []
            for r in results:
                context_parts.append(r['content'])
            
            context = "\n\n".join(context_parts) if context_parts else "No relevant information found in the database."
            
        except Exception as e:
            print(f"⚠️ Search error: {e}")
            context = "Unable to search the database at the moment."
        
        # Generate response with Groq (using updated model)
        system_prompt = """You are a friendly and knowledgeable local services assistant for India. 

Your role:
- Provide helpful, personalized recommendations based on the context provided
- Be conversational and warm in tone
- Include specific details like ratings, areas, and contact info when available
- If multiple options exist, briefly compare them
- If no exact match exists, suggest similar alternatives
- Always mention the city and area for each recommendation

Keep responses concise but informative. Be enthusiastic about helping people discover great local services!"""

        try:
            response = self.groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",  # Updated model
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Based on this information about local services:\n\n{context}\n\nUser question: {user_query}\n\nProvide a helpful, conversational response:"}
                ],
                temperature=0.7,
                max_tokens=600
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"

# Test function
if __name__ == "__main__":
    print("Testing RAG Engine...\n")
    
    rag = RAGEngine()
    
    print("\n" + "="*60)
    print("TEST QUERY")
    print("="*60)
    
    test_query = "Best restaurant in Bangalore for South Indian food"
    print(f"\nQuery: {test_query}\n")
    
    response = rag.query(test_query)
    print(f"Response:\n{response}")
    
    print("\n" + "="*60)