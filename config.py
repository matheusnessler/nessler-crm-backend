"""
Configurações do backend da interface web do CRM Nessler iStore.
Versão otimizada para deploy no Render.
"""
import os
from datetime import timedelta
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

class Config:
    """Configurações base da aplicação."""
    
    # Configurações do Flask
    SECRET_KEY = os.getenv("SECRET_KEY", "nessler_istore_secret_key_2025")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    # Configurações do banco de dados
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///crm_nessler.db")
    # Corrigir prefixo postgres:// para postgresql:// (necessário para o Render)
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configurações de JWT
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "nessler_istore_jwt_secret_2025")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    
    # Configurações de CORS
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:3000,https://nessleristore.com.br").split(",")
    
    # Configurações de integração com WhatsApp
    WHATSAPP_API_URL = os.getenv("WHATSAPP_API_URL", "https://graph.facebook.com/v17.0")
    WHATSAPP_PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID", "")
    WHATSAPP_ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN", "")
    
    # Configurações de integração com MercadoPhone
    MERCADOPHONE_API_URL = os.getenv("MERCADOPHONE_API_URL", "https://app.mercadophone.tech/api.php")
    MERCADOPHONE_API_TOKEN = os.getenv("MERCADOPHONE_API_TOKEN", "88c6d2b9-8b09-4411-aa59-d18fd506467f")

class DevelopmentConfig(Config):
    """Configurações para ambiente de desenvolvimento."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///crm_nessler_dev.db")
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

class TestingConfig(Config):
    """Configurações para ambiente de testes."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=5)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(seconds=10)

class ProductionConfig(Config):
    """Configurações para ambiente de produção."""
    DEBUG = False
    # Usar DATABASE_URL para compatibilidade com Render
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

# Dicionário de configurações por ambiente
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}

# Configuração ativa - usar FLASK_ENV ou RENDER para determinar ambiente
env = os.getenv("FLASK_ENV", "development")
if os.getenv("RENDER", "False").lower() == "true":
    env = "production"

active_config = config[env]
