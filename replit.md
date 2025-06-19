# Prateek's AI Assistant API

## Overview

This is a Flask-based API-only backend that serves as Prateek's personal AI assistant. The system answers questions about Prateek Savanur's professional experience, skills, projects, and background using a curated knowledge base and Groq's LLM for response generation. This API is designed to be deployed on Render and called from external frontend applications.

## System Architecture

### API Backend Architecture
- **Framework**: Flask REST API with CORS enabled for cross-origin requests
- **API Integration**: Groq API for language model inference (Llama3-8b-8192)
- **Knowledge Base**: In-memory curated knowledge base with comprehensive information about Prateek
- **Response Generation**: Intelligent context search with keyword mapping and AI-powered responses
- **Deployment**: Designed for Render deployment with environment variable configuration

## Key Components

### 1. Knowledge Base System (`api.py`)
- Curated, comprehensive knowledge base with sections: about, experience, projects, freelance, personal
- Intelligent keyword-based search to find relevant context for user queries
- Covers all aspects of Prateek's professional and personal background

### 2. API Endpoints
- **POST /api/chat**: Main endpoint for AI conversations about Prateek
- **GET /api/health**: Health check and system status endpoint
- **GET /**: API documentation and usage information

### 3. AI Response Generation
- **Context Search**: Smart keyword matching to retrieve relevant information
- **Prompt Engineering**: Structured prompts ensuring professional, accurate responses
- **Response Generation**: Groq's Llama3 model for generating detailed, contextual answers
- **Error Handling**: Comprehensive error handling with fallback responses

### 4. Data Coverage
The knowledge base includes:
- Professional background and current role at Eurofins IT Solutions
- Education and academic achievements
- Blockchain development projects (Stablecoin DeFi, Random NFT, DAO, Crowdfunding)
- Full-stack development experience and internships
- Freelance services and availability
- Personal interests, hobbies, and social links

## API Usage

### Request Format
```
POST /api/chat
Content-Type: application/json

{
  "message": "Tell me about Prateek's blockchain projects"
}
```

### Response Format
```json
{
  "response": "AI-generated response about Prateek",
  "sources": ["Prateek's Knowledge Base"],
  "error": null
}
```

### Data Flow
1. **Request Processing**: Frontend sends user query to /api/chat endpoint
2. **Context Search**: System searches knowledge base using keyword matching
3. **AI Generation**: Relevant context is sent to Groq API with structured prompt
4. **Response Delivery**: AI-generated response is returned to frontend application

## External Dependencies

### Required APIs
- **Groq API**: Language model inference (requires GROQ_API_KEY environment variable)
- **HuggingFace**: Embedding model (sentence-transformers/all-MiniLM-L6-v2)

### Python Packages
- Flask and Flask-CORS for API framework
- Requests for HTTP client functionality
- Gunicorn for production deployment

### Development Tools
- UV for dependency management
- Requirements.txt for Render deployment compatibility

## Deployment Strategy

### Render Deployment
- **Platform**: Render cloud platform for seamless deployment
- **Server**: Gunicorn WSGI server for production
- **Environment**: Python 3.11 with minimal dependencies
- **Port Configuration**: Dynamic port binding via PORT environment variable
- **CORS**: Configured for cross-origin requests from any frontend

### Environment Variables Required
- `GROQ_API_KEY`: Required for AI response generation
- `PORT`: Automatically set by Render (default: 5000)

### Deployment Files
- `requirements.txt`: Python dependencies for Render
- `api.py`: Main application file
- `main.py`: Entry point for the application

## Changelog

- June 19, 2025: Completed Render deployment configuration with all necessary files
- June 19, 2025: Converted to API-only backend for Render deployment  
- June 19, 2025: Initial setup with full-stack application

## User Preferences

- Preferred communication style: Simple, everyday language
- Deployment preference: API-only backend for Render, frontend hosted separately
- Focus: Clean, professional API responses about Prateek's background and expertise