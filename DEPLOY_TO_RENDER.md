# Deploy Prateek's AI Assistant to Render

## Quick Deployment Steps

### 1. Prepare Your Repository
1. Create a new GitHub repository
2. Upload these files:
   - `api.py` (main application)
   - `main.py` (entry point)
   - `requirements_render.txt` (dependencies)
   - `runtime.txt` (Python version)
   - `Procfile` (start command)

### 2. Deploy on Render
1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure:
   - **Name**: `prateeks-ai-assistant` (or your choice)
   - **Runtime**: Python 3
   - **Build Command**: `pip install Flask==3.1.1 Flask-CORS==6.0.1 gunicorn==23.0.0 requests==2.32.4`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT main:app`

### 3. Set Environment Variables
In Render dashboard, add:
- **Key**: `GROQ_API_KEY`
- **Value**: Your Groq API key

### 4. Deploy
Click **"Create Web Service"** - Render will automatically build and deploy.

## Your API Endpoints

After deployment, your API will be available at:
```
https://your-app-name.onrender.com
```

### Main Endpoints:
- `GET /` - API information
- `POST /api/chat` - Chat with AI about Prateek
- `GET /api/health` - Health check

## Frontend Integration Example

```javascript
// Replace with your actual Render URL
const API_URL = 'https://your-app-name.onrender.com';

async function askAboutPrateek(question) {
    const response = await fetch(`${API_URL}/api/chat`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: question })
    });
    
    const data = await response.json();
    return data.response;
}

// Usage
askAboutPrateek("What are Prateek's main skills?")
    .then(answer => console.log(answer));
```

## Files for Render Deployment

Make sure you have these exact files in your repository:

1. **requirements_render.txt**
```
Flask==3.1.1
Flask-CORS==6.0.1
gunicorn==23.0.0
requests==2.32.4
```

2. **Procfile**
```
web: gunicorn --bind 0.0.0.0:$PORT main:app
```

3. **runtime.txt**
```
python-3.11.10
```

## Testing Your Deployed API

```bash
# Test health check
curl https://your-app-name.onrender.com/api/health

# Test chat
curl -X POST https://your-app-name.onrender.com/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me about Prateek"}'
```

Your AI assistant will be live and ready to answer questions about you!