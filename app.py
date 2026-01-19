import streamlit as st
from rag_engine import RAGEngine
import time

# Page config
st.set_page_config(
    page_title="India Restaurants Finder",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #FF6B35;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        font-weight: 500;
    }
    .city-badge {
        display: inline-block;
        padding: 0.3rem 0.6rem;
        margin: 0.2rem;
        background-color: #f0f2f6;
        border-radius: 15px;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize RAG engine (cached so it only loads once)
@st.cache_resource
def init_rag():
    with st.spinner("🚀 Initializing AI Restaurant Finder... This may take a minute on first load..."):
        return RAGEngine()

# Main header
st.markdown('<div class="main-header">🍽️ All-India Restaurant Finder</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">AI-powered restaurant recommendations across India</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📍 Coverage")
    
    st.markdown("### 🏙️ Cities Covered")
    st.markdown("""
    <div style='line-height: 2;'>
    <span class='city-badge'>Ahmedabad</span>
    <span class='city-badge'>Bangalore</span>
    <span class='city-badge'>Bhubaneswar</span>
    <span class='city-badge'>Chandigarh</span>
    <span class='city-badge'>Chennai</span>
    <span class='city-badge'>Coimbatore</span>
    <span class='city-badge'>Delhi</span>
    <span class='city-badge'>Hyderabad</span>
    <span class='city-badge'>Indore</span>
    <span class='city-badge'>Jaipur</span>
    <span class='city-badge'>Kochi</span>
    <span class='city-badge'>Kolkata</span>
    <span class='city-badge'>Lucknow</span>
    <span class='city-badge'>Mumbai</span>
    <span class='city-badge'>Nagpur</span>
    <span class='city-badge'>Pune</span>
    <span class='city-badge'>Surat</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.header("🍴 What You Can Ask")
    st.markdown("""
    - Best restaurants in [city]
    - Where to eat [cuisine] in [city]
    - Top-rated cafes in [city]
    - Budget-friendly places in [city]
    - Highly rated food near [area]
    """)
    
    st.markdown("---")
    
    st.header("💡 Example Questions")
    
    example_queries = [
        "🍛 Best biryani in Hyderabad",
        "🍕 Top-rated restaurants in Bangalore",
        "☕ Good cafes in Pune",
        "🍜 Where to eat in Mumbai Bandra area",
        "🍲 North Indian food in Delhi",
        "🥘 Authentic local cuisine in Chennai",
        "💰 Budget-friendly restaurants in Ahmedabad",
        "⭐ Highest rated places in Kolkata"
    ]
    
    for example in example_queries:
        if st.button(example, key=example):
            st.session_state.example_query = example.split(" ", 1)[1]  # Remove emoji
    
    st.markdown("---")
    
    st.header("📊 Database Info")
    st.info("""
    **228 Restaurants** across **15+ cities**
    
    Data sourced from Kaggle's Swiggy Restaurant Dataset
    """)
    
    st.markdown("---")
    
    st.header("🔧 Tech Stack")
    st.markdown("""
    - **LLM:** Groq (LLaMA 3.3 70B)
    - **Vector DB:** Azure Cognitive Search
    - **Embeddings:** Sentence Transformers
    - **Data:** Google Sheets + Kaggle
    - **Architecture:** RAG (Retrieval Augmented Generation)
    """)
    
    st.markdown("---")
    
    if st.button("🔄 Reset Chat"):
        st.session_state.messages = []
        st.rerun()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Welcome message
if len(st.session_state.messages) == 0:
    welcome_msg = """👋 **Welcome to India Restaurant Finder!**

I can help you discover great restaurants across **15+ major Indian cities** including Bangalore, Mumbai, Delhi, Pune, Hyderabad, and more!

**Try asking:**
- "Best biryani restaurants in Hyderabad"
- "Top-rated cafes in Bangalore for working"
- "Where to eat in Mumbai Bandra area"
- "Budget-friendly restaurants in Pune"

What would you like to know?"""
    
    st.session_state.messages.append({"role": "assistant", "content": welcome_msg})

# Initialize RAG engine
try:
    rag = init_rag()
except Exception as e:
    st.error(f"❌ Error initializing RAG engine: {e}")
    st.stop()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle example query from sidebar
if "example_query" in st.session_state:
    prompt = st.session_state.example_query
    del st.session_state.example_query
else:
    prompt = st.chat_input("Ask about restaurants in any major Indian city...")

# Process user input
if prompt:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        with st.spinner("🔍 Searching restaurants across India..."):
            try:
                # Get response from RAG
                response = rag.query(prompt)
                
                # Display with typing effect (optional - makes it feel more interactive)
                full_response = ""
                for chunk in response.split():
                    full_response += chunk + " "
                    message_placeholder.markdown(full_response + "▌")
                    time.sleep(0.02)
                
                message_placeholder.markdown(response)
                
            except Exception as e:
                response = f"❌ Sorry, I encountered an error: {str(e)}"
                message_placeholder.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <small>🎓 Built for Inarva Solutions Internship Assessment | Powered by Azure AI + Groq + RAG Architecture</small><br>
    <small>📊 Data: Kaggle Swiggy Restaurant Dataset (228 restaurants across 15+ cities)</small>
</div>
""", unsafe_allow_html=True)