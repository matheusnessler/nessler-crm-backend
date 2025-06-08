"""
Modelo de usuário para autenticação no CRM da Nessler iStore.
Versão otimizada para deploy no Render.
"""
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    """Modelo de usuário para autenticação."""
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='user')
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, name, email, password, role='user'):
        """
        Inicializa um novo usuário.
        
        Args:
            name: Nome do usuário
            email: Email do usuário (único)
            password: Senha em texto plano
            role: Papel do usuário (default: 'user')
        """
        self.name = name
        self.email = email
        self.set_password(password)
        self.role = role
    
    def set_password(self, password):
        """
        Define a senha do usuário (hash).
        
        Args:
            password: Senha em texto plano
        """
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """
        Verifica se a senha está correta.
        
        Args:
            password: Senha em texto plano a verificar
            
        Returns:
            True se a senha estiver correta, False caso contrário
        """
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        """
        Converte o usuário para dicionário.
        
        Returns:
            Dicionário com os dados do usuário
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'active': self.active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    def __repr__(self):
        """Representação do usuário."""
        return f'<User {self.email}>'
