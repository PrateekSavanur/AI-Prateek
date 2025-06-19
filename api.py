import os
import logging
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Enable CORS for all origins (adjust for production)
CORS(app, origins=["*"])

# Knowledge base - comprehensive information about Prateek
KNOWLEDGE_BASE = {
    "about": """
Prateek Prasanna Savanur is a Blockchain developer with a strong foundation in decentralized technologies, cloud computing, and DevOps practices.

Education:
- Bachelor of Engineering in Computer Science and Engineering (Pursuing, Dayananda Sagar College of Engineering)
- CGPA: 9 (up to the 7th semester)

Skills & Expertise:
- Blockchain Development: Full-stack dApp development, smart contract creation, security best practices
- Platforms: Ethereum, Solana
- DevOps: CI/CD (Jenkins, Octopus Deploy), automation, workflow optimization
- Cloud Computing: AWS services for backend and decentralized systems
- Web Development: Full-stack web apps
- Tech Stack: React.js, Angular, Tailwind CSS, Node.js, Express.js, MongoDB, .NET, Azure, AWS, Docker, Kubernetes

Current Role:
Associate Software Engineer at Eurofins IT Solutions, working full-time in DevOps while exploring freelance opportunities.

Contact: prateeksavanur@duck.com
Website: https://prateeksavanur.xyz/
""",
    
    "experience": """
Professional Experience:

Current Role:
- Associate Software Engineer at Eurofins IT Solutions (DevOps field)
- Managing deployment pipelines and automating infrastructure
- Implementing cloud-based solutions using AWS and Azure
- Open to part-time freelance work in Ethereum, Solana, Full-stack development

Internships:
1. Frontend Developer at H2SO4-Labs (15/07/2024 – 15/09/2024)
   - Built responsive UI components with React.js
   - Collaborated on API integration for dynamic web applications

2. Blockchain Developer Intern at 2x Solutions (01/09/2023 – 31/12/2023)
   - Developed and optimized secure smart contracts
   - Conducted audits for vulnerabilities
   - Integrated Chainlink oracles for external data feeds

3. Technical Consultant at Knit Finance (15/05/2023 – 31/08/2023)
   - Created educational content on Blockchain
   - Explored emerging technologies

Volunteer Experience:
- Chapter Lead at TPG Karnataka (01/2024 – Present)
- Organizing blockchain events and engaging with professionals
""",

    "projects": """
Major Projects:

1. Stablecoin DeFi System
   - DAI-inspired stablecoin system with Chainlink oracles for price feeds
   - Implemented automated liquidation and redemption processes
   - Tech: Solidity, Foundry, Chainlink Oracle
   - GitHub: https://github.com/PrateekSavanur/Stablecoin-DeFi.git

2. Random NFT Generator
   - Built using Chainlink VRF for secure randomness
   - Integrated Pinata for decentralized storage
   - Tech: Solidity, Hardhat, Chainlink Oracles
   - GitHub: https://github.com/PrateekSavanur/NFT-Hardhat

3. Swapify - Barter System
   - MERN stack-based platform for exchanging goods/services
   - JWT-based authentication and MongoDB for data persistence
   - GitHub Backend: https://github.com/PrateekSavanur/Barter-Backend
   - GitHub Frontend: https://github.com/PrateekSavanur/Barter-Frontend
   - Live API: https://barter-backend-five.vercel.app/
   - API Documentation: https://documenter.getpostman.com/view/31551887/2sAYQanBmZ

4. Crowdfunding DApp
   - Blockchain-based crowdfunding platform with smart contracts
   - Project creation, funding, and token distribution features
   - Uses TokenFactory for creating reward tokens
   - Tech: Solidity, Foundry, Wagmi, React.js

5. DAO (Decentralized Autonomous Organization)
   - Governance system with Governor contract and governance token (GovToken)
   - Proposal creation, voting, and execution mechanisms
   - Tech: Solidity, OpenZeppelin, Foundry
   - GitHub: https://github.com/PrateekSavanur/Foundry-DAO.git

6. Event Management Contract
   - Solidity contract for creating events and selling tickets
   - Features ticket purchasing, transferring, and event management
   - Ethereum-based smart contract system

7. Other Projects:
   - Token Swap DApp (React.js, Express.js, Moralis, 1inch)
   - Audio NFT Generator (Solidity, IPFS, React.js, Wagmi)
   - Journal Solana (Solana, Rust, React.js)
   - Crypto Wallet Extension (Chrome Extensions, React.js)
   - Tours Website (React.js, Node.js, Express.js, MongoDB)
""",

    "freelance": """
Freelance Services & Availability:

Prateek is available for part-time freelance work while working full-time at Eurofins IT Solutions.

1. Full-Stack Web Development
   - Responsive and dynamic web applications
   - Frontend & backend integration
   - REST APIs & GraphQL APIs
   - Authentication & Authorization (JWT, OAuth)
   - Cloud hosting & CI/CD setup
   - Tech: React.js, Next.js, Angular, Tailwind CSS, Node.js, Express.js, .NET Core, MongoDB, PostgreSQL, Firebase, Docker, Kubernetes, AWS, Azure

2. Blockchain Development
   - Smart contract development & deployment
   - DApps with wallet integrations (Metamask, Phantom)
   - Chainlink Oracles & VRF integration
   - NFT platforms & marketplaces
   - Token creation (ERC-20, ERC-721, ERC-1155)
   - Auditing & security best practices
   - Tech: Ethereum (Solidity, Hardhat, Foundry, Ethers.js), Solana (Rust, Anchor), Chainlink, OpenZeppelin, IPFS, Wagmi

3. Hybrid Projects
   - Full-stack DApps with blockchain backend
   - MERN/MEAN stack + smart contract integration
   - Custom DAO & DeFi apps
   - Web3.js & Ethers.js integrations

Additional Services:
- Smart Contract Audits
- CI/CD Pipeline Setup (Octopus, Jenkins, GitHub Actions)
- Hosting & Deployment (AWS, Azure, Netlify, Vercel)
- Custom Web3 Education & Documentation

Why Choose Prateek:
- Proven experience across multiple blockchain & fullstack projects
- Clean, scalable, and secure code delivery
- Agile communication & milestone-based deliveries
- Flexible with timezone & collaborative in feedback cycles

Contact: prateeksavanur@duck.com
Website: https://prateeksavanur.xyz/
""",

    "personal": """
Personal Interests & Background:

Hobbies & Interests:
- Watching favorite shows: Breaking Bad, Game of Thrones, Friends, Taarak Mehta Ka Ooltah Chashmah (TMKOC), Peaky Blinders, Money Heist, The Boys, Narcos
- Playing music: Guitar, Flute, Singing
- Passionate about: Space exploration (huge fan of SpaceX & ISRO), Crypto, finance, and tech trends
- Occasionally: Reading fiction, Catching up on memes

Vision & Philosophy:
Prateek is passionate about the intersection of finance and technology, particularly the transformative potential of decentralized finance (DeFi). He aims to build innovative blockchain-powered financial solutions that challenge traditional systems and empower people globally.

Fun Fact:
Prateek once debugged a smart contract at 3 AM with coffee in one hand and guitar in the other – productivity + vibes combo.

Social Links:
- Website: https://prateeksavanur.xyz/
- Linktree: https://linktr.ee/prateeksavanur
- LinkedIn: https://www.linkedin.com/in/prateeksavanur
- Portfolio: https://prateeksavanur.netlify.app/
- Twitter: https://x.com/prateek_savanur
- GitHub: https://github.com/PrateekSavanur
- Leetcode: https://leetcode.com/Prateek_savanur/
- Medium: https://prateeksavanur.medium.com/
"""
}

def search_knowledge_base(query):
    """Search through the knowledge base for relevant information"""
    query_lower = query.lower()
    relevant_sections = []
    
    # Keywords to section mapping
    keywords = {
        "about": ["who", "about", "background", "education", "skills", "expertise", "prateek"],
        "experience": ["experience", "work", "job", "internship", "role", "company", "eurofins", "devops", "career"],
        "projects": ["project", "github", "code", "built", "created", "stablecoin", "nft", "dao", "crowdfunding", "swapify", "barter", "portfolio"],
        "freelance": ["freelance", "hire", "services", "contact", "work", "available", "price", "cost", "consulting"],
        "personal": ["hobby", "interest", "music", "guitar", "shows", "personal", "fun", "space", "spacex", "hobbies"]
    }
    
    # Find relevant sections based on keywords
    for section, section_keywords in keywords.items():
        if any(keyword in query_lower for keyword in section_keywords):
            relevant_sections.append(section)
    
    # If no specific keywords found, include most relevant sections
    if not relevant_sections:
        relevant_sections = ["about", "experience", "projects"]
    
    # Combine relevant information
    context = ""
    for section in relevant_sections:
        context += f"\n\n{KNOWLEDGE_BASE[section]}"
    
    return context.strip()

def generate_response_with_groq(query, context):
    """Generate response using Groq API"""
    groq_api_key = os.getenv("GROQ_API_KEY")
    
    if not groq_api_key:
        return "I apologize, but I'm currently unable to process your request. Please contact Prateek directly at prateeksavanur@duck.com."
    
    prompt = f"""You are Prateek's AI assistant. Answer questions about Prateek Savanur based only on the following context.

Context:
{context}

Question: {query}

Instructions:
- Provide a detailed, comprehensive response about Prateek
- When referring to Prateek, use third person ("Prateek is...", "He has experience in...", etc.)
- If asked about who you are, clearly state that you are Prateek's AI assistant
- Answer only based on the provided context
- Be professional and knowledgeable
- If information isn't in the context, say you don't have that information
- Include relevant details about Prateek's skills, projects, and experience
- Keep responses focused and informative

Answer:"""

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {groq_api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama3-8b-8192",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 512,
                "temperature": 0.3
            },
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            logger.error(f"Groq API error: {response.status_code} - {response.text}")
            return "I apologize, but I'm having trouble processing your request right now. Please contact Prateek directly at prateeksavanur@duck.com."
            
    except Exception as e:
        logger.error(f"Error calling Groq API: {e}")
        return "I apologize, but I'm having trouble processing your request right now. Please contact Prateek directly at prateeksavanur@duck.com."

@app.route('/', methods=['GET'])
def home():
    """API information endpoint"""
    return jsonify({
        "message": "Prateek's AI Assistant API",
        "version": "1.0.0",
        "endpoints": {
            "POST /api/chat": "Main chat endpoint - send message to get AI response",
            "GET /api/health": "Health check endpoint"
        },
        "usage": {
            "chat": {
                "method": "POST",
                "url": "/api/chat",
                "body": {"message": "Your question about Prateek"},
                "response": {"response": "AI response", "sources": ["source"], "error": None}
            }
        }
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """Main chat endpoint for the AI assistant"""
    try:
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
        
        logger.info(f"Processing query: {query_text}")
        
        # Search knowledge base for relevant context
        context = search_knowledge_base(query_text)
        
        # Generate response using Groq
        response_text = generate_response_with_groq(query_text, context)
        
        return jsonify({
            "response": response_text,
            "sources": ["Prateek's Knowledge Base"],
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
    groq_api_key = os.getenv("GROQ_API_KEY")
    
    status = {
        "status": "healthy",
        "api_version": "1.0.0",
        "model": "available" if groq_api_key else "unavailable",
        "groq_api_key": "configured" if groq_api_key else "missing",
        "knowledge_base": "loaded",
        "endpoints": ["POST /api/chat", "GET /api/health"]
    }
    return jsonify(status)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)