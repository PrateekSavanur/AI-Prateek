import os
import logging
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pydantic import BaseModel
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "your-secret-key-here")

# Enable CORS for all routes
CORS(app, origins=["*"])

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
You are Prateek's AI assistant. Answer questions about Prateek Savanur based only on the following context.

Context:
{context}

---

Please provide a detailed, comprehensive response about Prateek to the following question. 
When referring to Prateek, use third person ("Prateek is...", "He has experience in...", etc.).
If you're asked about who you are, clearly state that you are Prateek's AI assistant.

Key guidelines:
- Answer only based on the provided context
- Be professional and knowledgeable
- If information isn't in the context, say you don't have that information
- Include relevant details about Prateek's skills, projects, and experience
- Keep responses focused and informative

Question: {question}

Answer:
"""

# Initialize components
try:
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        logger.warning("GROQ_API_KEY not found in environment variables")
    
    # Initialize embeddings and database
    embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Check if ChromaDB exists
    if os.path.exists(CHROMA_PATH):
        db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
        logger.info("ChromaDB loaded successfully")
    else:
        logger.warning("ChromaDB not found. Run create_database.py first.")
        db = None
    
    # Initialize Groq model
    if groq_api_key:
        model = ChatGroq(
            api_key=groq_api_key,
            model_name="llama3-8b-8192",
            max_tokens=512,
            temperature=0.3,
        )
        logger.info("Groq model initialized successfully")
    else:
        model = None
        logger.error("Groq model not initialized - missing API key")

except Exception as e:
    logger.error(f"Error initializing components: {e}")
    db = None
    model = None

@app.route('/')
def index():
    """Serve the main chat interface"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Main chat endpoint for the AI assistant"""
    try:
        # Get the query from request
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({
                "error": "Missing 'message' in request body",
                "response": None,
                "sources": []
            }), 400
        
        query_text = data['message'].strip()
        if not query_text:
            return jsonify({
                "error": "Empty message provided",
                "response": None,
                "sources": []
            }), 400
        
        # Check if components are initialized
        if not db:
            return jsonify({
                "error": "Knowledge base not available. Please contact the administrator.",
                "response": "I'm sorry, but I'm currently unable to access my knowledge base. Please try again later or contact Prateek directly at prateeksavanur@duck.com.",
                "sources": []
            }), 500
        
        if not model:
            return jsonify({
                "error": "AI model not available. Please contact the administrator.",
                "response": "I'm sorry, but I'm currently unable to process your request. Please try again later or contact Prateek directly at prateeksavanur@duck.com.",
                "sources": []
            }), 500
        
        # Perform similarity search
        results = db.similarity_search(query_text, k=5)
        
        if not results:
            return jsonify({
                "response": "I don't have information about that in my current knowledge base. For specific inquiries, please contact Prateek directly at prateeksavanur@duck.com.",
                "sources": [],
                "error": None
            })
        
        # Prepare context
        context_text = "\n\n---\n\n".join([doc.page_content for doc in results])
        
        # Create prompt
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=query_text)
        
        # Query the model
        response_text = model.predict(prompt)
        
        # Collect sources
        sources = []
        for doc in results:
            source = doc.metadata.get("source", "Unknown source")
            if source not in sources:
                sources.append(source)
        
        return jsonify({
            "response": response_text,
            "sources": sources[:3],  # Limit to top 3 sources
            "error": None
        })
    
    except Exception as e:
        logger.error(f"Error processing chat request: {e}")
        return jsonify({
            "error": f"An error occurred: {str(e)}",
            "response": "I apologize, but I encountered an error while processing your request. Please try again or contact Prateek directly at prateeksavanur@duck.com.",
            "sources": []
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    status = {
        "status": "healthy",
        "database": "available" if db else "unavailable",
        "model": "available" if model else "unavailable",
        "groq_api_key": "configured" if os.getenv("GROQ_API_KEY") else "missing"
    }
    return jsonify(status)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
