from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()

class ConversationSession(db.Model):
    __tablename__ = 'conversation_sessions'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_activity = db.Column(db.DateTime, default=datetime.utcnow)
    context_summary = db.Column(db.Text)
    total_messages = db.Column(db.Integer, default=0)
    
    # Relationship to messages
    messages = db.relationship('ConversationMessage', backref='session', cascade='all, delete-orphan')

class ConversationMessage(db.Model):
    __tablename__ = 'conversation_messages'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(36), db.ForeignKey('conversation_sessions.id'), nullable=False)
    message_type = db.Column(db.String(10), nullable=False)  # 'user' or 'assistant'
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    topics = db.Column(db.String(500))  # Comma-separated list of topics discussed

class KnowledgeUpdate(db.Model):
    __tablename__ = 'knowledge_updates'
    
    id = db.Column(db.Integer, primary_key=True)
    update_type = db.Column(db.String(50), nullable=False)  # 'project', 'achievement', 'experience', etc.
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    priority = db.Column(db.Integer, default=1)  # 1-5, higher = more important

class FreelanceAvailability(db.Model):
    __tablename__ = 'freelance_availability'
    
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), nullable=False)  # 'available', 'busy', 'limited'
    hours_per_week = db.Column(db.Integer)
    preferred_project_types = db.Column(db.String(500))
    current_rate_range = db.Column(db.String(100))
    availability_notes = db.Column(db.Text)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_current = db.Column(db.Boolean, default=True)