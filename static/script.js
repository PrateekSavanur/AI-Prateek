class ChatApp {
    constructor() {
        this.chatMessages = document.getElementById('chat-messages');
        this.messageInput = document.getElementById('message-input');
        this.sendButton = document.getElementById('send-button');
        this.statusIndicator = document.getElementById('status-indicator');
        this.statusText = document.getElementById('status-text');
        
        this.isLoading = false;
        
        this.init();
    }
    
    init() {
        // Event listeners
        this.sendButton.addEventListener('click', () => this.sendMessage());
        this.messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });
        
        // Sample question buttons
        document.querySelectorAll('.sample-question').forEach(button => {
            button.addEventListener('click', (e) => {
                const question = e.target.getAttribute('data-question');
                this.messageInput.value = question;
                this.sendMessage();
            });
        });
        
        // Check health status
        this.checkHealth();
        
        // Auto-focus input
        this.messageInput.focus();
    }
    
    async checkHealth() {
        try {
            const response = await fetch('/api/health');
            const data = await response.json();
            
            if (data.status === 'healthy' && data.database === 'available' && data.model === 'available') {
                this.setStatus('online', 'Ready to chat');
            } else {
                this.setStatus('offline', 'System unavailable');
            }
        } catch (error) {
            console.error('Health check failed:', error);
            this.setStatus('offline', 'Connection error');
        }
    }
    
    setStatus(status, text) {
        this.statusIndicator.className = `status-indicator ${status === 'offline' ? 'offline' : ''}`;
        this.statusText.textContent = text;
    }
    
    async sendMessage() {
        const message = this.messageInput.value.trim();
        
        if (!message || this.isLoading) {
            return;
        }
        
        // Add user message to chat
        this.addMessage(message, 'user');
        this.messageInput.value = '';
        
        // Show loading state
        this.setLoading(true);
        this.showTypingIndicator();
        
        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });
            
            const data = await response.json();
            
            // Remove typing indicator
            this.removeTypingIndicator();
            
            if (data.response) {
                this.addMessage(data.response, 'ai', data.sources);
            } else {
                this.addMessage(
                    data.error || 'Sorry, I encountered an error processing your request.',
                    'ai'
                );
            }
        } catch (error) {
            console.error('Chat error:', error);
            this.removeTypingIndicator();
            this.addMessage(
                'Sorry, I\'m having trouble connecting. Please try again later.',
                'ai'
            );
        } finally {
            this.setLoading(false);
        }
    }
    
    addMessage(text, type, sources = []) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}-message`;
        
        const avatar = document.createElement('div');
        avatar.className = 'message-avatar';
        avatar.innerHTML = type === 'user' ? '<i class="fas fa-user"></i>' : '<i class="fas fa-robot"></i>';
        
        const content = document.createElement('div');
        content.className = 'message-content';
        
        const messageText = document.createElement('div');
        messageText.className = 'message-text';
        messageText.textContent = text;
        
        const messageTime = document.createElement('div');
        messageTime.className = 'message-time';
        messageTime.textContent = this.getCurrentTime();
        
        content.appendChild(messageText);
        content.appendChild(messageTime);
        
        // Add sources if available
        if (sources && sources.length > 0) {
            const sourcesDiv = document.createElement('div');
            sourcesDiv.className = 'message-sources';
            sourcesDiv.innerHTML = '<small class="text-muted">Sources: </small>';
            
            sources.forEach(source => {
                const badge = document.createElement('span');
                badge.className = 'badge bg-secondary';
                badge.textContent = source;
                sourcesDiv.appendChild(badge);
            });
            
            content.appendChild(sourcesDiv);
        }
        
        messageDiv.appendChild(avatar);
        messageDiv.appendChild(content);
        
        this.chatMessages.appendChild(messageDiv);
        this.scrollToBottom();
    }
    
    showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message ai-message typing-indicator';
        typingDiv.id = 'typing-indicator';
        
        typingDiv.innerHTML = `
            <div class="message-avatar">
                <i class="fas fa-robot"></i>
            </div>
            <div class="typing-dots">
                <span></span>
                <span></span>
                <span></span>
            </div>
        `;
        
        this.chatMessages.appendChild(typingDiv);
        this.scrollToBottom();
    }
    
    removeTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }
    
    setLoading(loading) {
        this.isLoading = loading;
        this.sendButton.disabled = loading;
        this.messageInput.disabled = loading;
        
        if (loading) {
            this.sendButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
        } else {
            this.sendButton.innerHTML = '<i class="fas fa-paper-plane"></i>';
        }
    }
    
    scrollToBottom() {
        this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
    }
    
    getCurrentTime() {
        return new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }
}

// Initialize the chat app when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new ChatApp();
});
