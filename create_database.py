import os
import logging
from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CHROMA_PATH = "chroma"
DATA_PATH = "data"

def main():
    """Generate the ChromaDB database from documents in the data directory."""
    
    # Check if data directory exists
    if not os.path.exists(DATA_PATH):
        logger.error(f"Data directory '{DATA_PATH}' not found!")
        return
    
    # Generate documents
    documents = generate_data_store()
    if not documents:
        logger.error("No documents found to process!")
        return
    
    # Save to ChromaDB
    save_to_chroma(documents)
    logger.info("Database creation completed successfully!")

def generate_data_store():
    """Load and split documents from the data directory."""
    try:
        # Load documents from the data directory
        loader = DirectoryLoader(DATA_PATH, glob="*.md")
        documents = loader.load()
        
        if not documents:
            logger.warning("No documents found in data directory")
            return []
        
        logger.info(f"Loaded {len(documents)} documents")
        
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=80,
            length_function=len,
            add_start_index=True,
        )
        chunks = text_splitter.split_documents(documents)
        
        logger.info(f"Split into {len(chunks)} chunks")
        
        # Add metadata to chunks
        for i, chunk in enumerate(chunks):
            # Extract filename from source path
            source_path = chunk.metadata.get("source", "")
            filename = os.path.basename(source_path)
            chunk.metadata["source"] = filename
            chunk.metadata["chunk_id"] = i
        
        return chunks
    
    except Exception as e:
        logger.error(f"Error generating data store: {e}")
        return []

def save_to_chroma(chunks):
    """Save document chunks to ChromaDB."""
    try:
        # Clear out the database first if it exists
        if os.path.exists(CHROMA_PATH):
            import shutil
            shutil.rmtree(CHROMA_PATH)
            logger.info("Cleared existing ChromaDB")
        
        # Create the new DB from the documents
        embedding_function = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        db = Chroma.from_documents(
            chunks,
            embedding_function,
            persist_directory=CHROMA_PATH
        )
        
        logger.info(f"Saved {len(chunks)} chunks to ChromaDB at {CHROMA_PATH}")
        
        # Test the database
        test_query = "Who is Prateek?"
        results = db.similarity_search(test_query, k=3)
        logger.info(f"Database test successful - found {len(results)} results for test query")
        
    except Exception as e:
        logger.error(f"Error saving to ChromaDB: {e}")
        raise

if __name__ == "__main__":
    main()
