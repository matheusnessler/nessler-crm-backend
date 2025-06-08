"""
Inicialização da aplicação Flask para o CRM da Nessler iStore.
Versão otimizada para deploy no Render.
"""
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
import os

# Inicialização de extensões
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def create_app(config_class=None):
    """
    Cria e configura uma instância da aplicação Flask.
    
    Args:
        config_class: Classe de configuração a ser utilizada
        
    Returns:
        Aplicação Flask configurada
    """
    # Criar aplicação Flask
    app = Flask(__name__, static_folder='../frontend', static_url_path='')
    
    # Carregar configurações
    if config_class is None:
        from config import active_config
        app.config.from_object(active_config)
    else:
        app.config.from_object(config_class)
    
    # Inicializar extensões
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    
    # Configurar CORS
    CORS(app, resources={r"/api/*": {"origins": app.config["CORS_ORIGINS"]}})
    
    # Registrar blueprints
    from app.routes.auth import auth_bp
    from app.routes.clients import clients_bp
    from app.routes.products import products_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.webhook import webhook_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(clients_bp, url_prefix="/api/clients")
    app.register_blueprint(products_bp, url_prefix="/api/products")
    app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")
    app.register_blueprint(webhook_bp)  # ✅ Agora está dentro da função correta

    # Rota de verificação de saúde
    @app.route("/api/health")
    def health_check():
        return {"status": "online", "message": "CRM Nessler iStore API está funcionando!"}
    
    # Servir frontend estático
    @app.route('/')
    def serve_frontend():
        return send_from_directory(app.static_folder, 'index.html')
    
    @app.route('/<path:path>')
    def serve_frontend_paths(path):
        if os.path.exists(os.path.join(app.static_folder, path)):
            return send_from_directory(app.static_folder, path)
        return send_from_directory(app.static_folder, 'index.html')

    return app
