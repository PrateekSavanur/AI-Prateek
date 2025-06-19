# Prateek's AI Assistant

## Overview

This is a Flask-based AI assistant application that serves as a personal assistant for Prateek Savanur. The system uses Retrieval-Augmented Generation (RAG) to answer questions about Prateek's professional experience, skills, projects, and background. The application leverages ChromaDB for document storage and retrieval, HuggingFace embeddings for semantic search, and Groq's LLM for response generation.

## System Architecture

### Backend Architecture
- **Framework**: Flask web application with CORS enabled
- **API Integration**: Groq API for language model inference (Llama3-8b-8192)
- **Document Processing**: LangChain for document loading, text splitting, and prompt management
- **Embeddings**: HuggingFace sentence-transformers (all-MiniLM-L6-v2)
- **Vector Database**: ChromaDB for storing and retrieving document embeddings
- **Data Source**: Markdown files containing Prateek's professional information

### Frontend Architecture
- **Framework**: Vanilla JavaScript with Bootstrap for UI components
- **Styling**: Bootstrap dark theme with custom CSS
- **Real-time Communication**: Fetch API for REST communication
- **User Interface**: Chat-based interface with sidebar navigation and sample questions

## Key Components

### 1. Document Processing System (`create_database.py`)
- Loads markdown documents from the `data/` directory
- Splits documents into chunks (800 characters with 80 character overlap)
- Generates embeddings using HuggingFace transformers
- Stores embeddings in ChromaDB for efficient retrieval

### 2. RAG Pipeline (`app.py`)
- **Document Retrieval**: Searches ChromaDB for relevant context based on user queries
- **Prompt Engineering**: Uses structured prompt template to ensure consistent, professional responses
- **Response Generation**: Leverages Groq's Llama3 model for generating detailed answers
- **Context Management**: Maintains conversation context while focusing on Prateek's information

### 3. Web Interface
- **Chat Interface**: Real-time messaging system with typing indicators
- **Sample Questions**: Pre-defined questions to guide user interactions
- **Status Monitoring**: Health check system to verify API and database availability
- **Responsive Design**: Mobile-friendly interface with sidebar navigation

### 4. Data Layer
The system contains comprehensive information about Prateek including:
- Professional background and education
- Blockchain development projects (Ethereum, Solana)
- Smart contract projects (Crowdfunding, DAO, Stablecoin, Event Management)
- Full-stack development experience
- Skills and technical expertise
- Personal interests and hobbies

## Data Flow

1. **Initialization**: Application loads ChromaDB database and initializes embeddings model
2. **Query Processing**: User submits question through web interface
3. **Document Retrieval**: System searches ChromaDB for relevant context using semantic similarity
4. **Response Generation**: Retrieved context is injected into prompt template and sent to Groq API
5. **Response Delivery**: Generated response is returned to user through the web interface
6. **Health Monitoring**: System continuously monitors API availability and database status

## External Dependencies

### Required APIs
- **Groq API**: Language model inference (requires GROQ_API_KEY environment variable)
- **HuggingFace**: Embedding model (sentence-transformers/all-MiniLM-L6-v2)

### Python Packages
- Flask and Flask-CORS for web framework
- LangChain ecosystem for RAG pipeline
- ChromaDB for vector storage
- Pydantic for data validation
- Gunicorn for production deployment

### Development Tools
- UV for dependency management
- PostgreSQL included in Nix configuration (for potential future database needs)

## Deployment Strategy

### Production Configuration
- **Server**: Gunicorn WSGI server with auto-scaling deployment target
- **Platform**: Replit with Nix package management
- **Environment**: Python 3.11 with required system packages
- **Port Configuration**: Binds to 0.0.0.0:5000 with port reuse enabled
- **Process Management**: Parallel workflow execution with reload capability

### Environment Setup
- Nix channel: stable-24_05 with essential packages (bash, libxcrypt, openssl, postgresql)
- Containerized deployment ready with Gunicorn configuration
- Development mode supports hot reload for iterative development

## Changelog

- June 19, 2025. Initial setup

## User Preferences

Preferred communication style: Simple, everyday language.