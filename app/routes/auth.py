"""
Rotas de autenticação para o CRM da Nessler iStore.
Versão otimizada para deploy no Render.
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from app import db
from app.models.user import User

# Criar blueprint
auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    """Rota para autenticação de usuários."""
    # Obter dados da requisição
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Dados não fornecidos"}), 400
    
    email = data.get("email")
    password = data.get("password")
    
    if not email or not password:
        return jsonify({"error": "Email e senha são obrigatórios"}), 400
    
    # Buscar usuário pelo email
    user = User.query.filter_by(email=email).first()
    
    # Verificar se o usuário existe e a senha está correta
    if not user or not user.check_password(password):
        return jsonify({"error": "Email ou senha incorretos"}), 401
    
    # Verificar se o usuário está ativo
    if not user.active:
        return jsonify({"error": "Usuário inativo"}), 403
    
    # Gerar tokens
    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    
    # Retornar tokens e dados do usuário
    return jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token,
        "user": user.to_dict()
    }), 200

@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    """Rota para renovação de token de acesso."""
    # Obter identidade do usuário
    user_id = get_jwt_identity()
    
    # Buscar usuário
    user = User.query.get(user_id)
    
    if not user or not user.active:
        return jsonify({"error": "Usuário não encontrado ou inativo"}), 401
    
    # Gerar novo token de acesso
    access_token = create_access_token(identity=user_id)
    
    # Retornar novo token
    return jsonify({
        "access_token": access_token
    }), 200

@auth_bp.route("/register", methods=["POST"])
@jwt_required()
def register():
    """Rota para registro de novos usuários (apenas para administradores)."""
    # Obter identidade do usuário atual
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    
    # Verificar se o usuário atual é administrador
    if not current_user or current_user.role != "admin":
        return jsonify({"error": "Permissão negada"}), 403
    
    # Obter dados da requisição
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Dados não fornecidos"}), 400
    
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role", "user")
    
    if not name or not email or not password:
        return jsonify({"error": "Nome, email e senha são obrigatórios"}), 400
    
    # Verificar se o email já está em uso
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email já está em uso"}), 400
    
    # Criar novo usuário
    user = User(name=name, email=email, password=password, role=role)
    
    # Salvar no banco de dados
    db.session.add(user)
    db.session.commit()
    
    # Retornar dados do usuário criado
    return jsonify({
        "message": "Usuário criado com sucesso",
        "user": user.to_dict()
    }), 201

@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def me():
    """Rota para obter dados do usuário autenticado."""
    # Obter identidade do usuário
    user_id = get_jwt_identity()
    
    # Buscar usuário
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    
    # Retornar dados do usuário
    return jsonify(user.to_dict()), 200

@auth_bp.route("/change-password", methods=["POST"])
@jwt_required()
def change_password():
    """Rota para alteração de senha."""
    # Obter identidade do usuário
    user_id = get_jwt_identity()
    
    # Buscar usuário
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    
    # Obter dados da requisição
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Dados não fornecidos"}), 400
    
    current_password = data.get("current_password")
    new_password = data.get("new_password")
    
    if not current_password or not new_password:
        return jsonify({"error": "Senha atual e nova senha são obrigatórias"}), 400
    
    # Verificar se a senha atual está correta
    if not user.check_password(current_password):
        return jsonify({"error": "Senha atual incorreta"}), 401
    
    # Atualizar senha
    user.set_password(new_password)
    db.session.commit()
    
    return jsonify({"message": "Senha alterada com sucesso"}), 200
