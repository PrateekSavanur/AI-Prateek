# Prateek's AI Assistant API

A Flask-based REST API that serves as Prateek Savanur's personal AI assistant. This API provides intelligent responses about Prateek's professional background, skills, projects, and experience.

## 🚀 Quick Start

### Deploy to Render

1. **Fork/Clone this repository**
2. **Connect to Render:**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New" → "Web Service"
   - Connect your GitHub repository
3. **Configure Environment:**
   - Set `GROQ_API_KEY` in environment variables
   - Render will automatically detect Python and use the build settings
4. **Deploy:**
   - Render will automatically build and deploy your API

### Environment Variables

- `GROQ_API_KEY` (Required): Your Groq API key for AI responses
- `PORT` (Automatic): Set by Render, defaults to 10000

## 📡 API Endpoints

### Base URL
```
https://your-app-name.onrender.com
```

### Endpoints

#### 1. Get API Information
```http
GET /
```

**Response:**
```json
{
  "message": "Prateek's AI Assistant API",
  "version": "1.0.0",
  "endpoints": {
    "POST /api/chat": "Main chat endpoint",
    "GET /api/health": "Health check endpoint"
  }
}
```

#### 2. Chat with AI Assistant
```http
POST /api/chat
Content-Type: application/json

{
  "message": "Tell me about Prateek's blockchain projects"
}
```

**Response:**
```json
{
  "response": "Prateek has worked on several impressive blockchain projects including...",
  "sources": ["Prateek's Knowledge Base"],
  "error": null
}
```

#### 3. Health Check
```http
GET /api/health
```

**Response:**
```json
{
  "status": "healthy",
  "api_version": "1.0.0",
  "model": "available",
  "groq_api_key": "configured",
  "knowledge_base": "loaded"
}
```

## 🔧 Frontend Integration

### JavaScript Example
```javascript
const API_BASE_URL = 'https://your-app-name.onrender.com';

async function askPrateekAI(message) {
  try {
    const response = await fetch(`${API_BASE_URL}/api/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    });
    
    const data = await response.json();
    return data.response;
  } catch (error) {
    console.error('Error:', error);
    return 'Sorry, I had trouble processing your request.';
  }
}

// Usage
askPrateekAI("What are Prateek's main skills?")
  .then(response => console.log(response));
```

### React Example
```jsx
import { useState } from 'react';

const API_BASE_URL = 'https://your-app-name.onrender.com';

function PrateekAIChat() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      const res = await fetch(`${API_BASE_URL}/api/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message }),
      });
      
      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      setResponse('Error connecting to AI assistant');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Ask about Prateek..."
          disabled={loading}
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Asking...' : 'Ask AI'}
        </button>
      </form>
      {response && <div>{response}</div>}
    </div>
  );
}
```

## 🧠 Knowledge Base

The AI has comprehensive knowledge about:

- **Professional Background**: Current role at Eurofins IT Solutions, education, skills
- **Experience**: Internships, volunteer work, career progression
- **Projects**: Blockchain projects (Stablecoin DeFi, NFT Generator, DAO), full-stack applications
- **Skills**: Blockchain development (Ethereum, Solana), DevOps, full-stack development
- **Freelance Services**: Available services and expertise areas
- **Personal**: Hobbies, interests, and personality

## 🔒 CORS Configuration

The API is configured with CORS enabled for all origins, making it suitable for frontend applications hosted on any domain.

## 🛠️ Local Development

```bash
# Clone repository
git clone <your-repo-url>
cd prateeks-ai-api

# Install dependencies
pip install -r requirements.txt

# Set environment variable
export GROQ_API_KEY="your-groq-api-key"

# Run locally
python main.py
```

## 📞 Support

For issues or questions:
- Email: prateeksavanur@duck.com
- Website: https://prateeksavanur.xyz/

---

Built with ❤️ for seamless AI assistant integration