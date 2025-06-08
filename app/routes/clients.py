"""
Rotas para gerenciamento de clientes no CRM da Nessler iStore.
Versão otimizada para deploy no Render.
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.user import User

# Criar blueprint
clients_bp = Blueprint("clients", __name__)

@clients_bp.route("/", methods=["GET"])
@jwt_required()
def get_clients():
    """Rota para listar clientes do MercadoPhone."""
    # Simulação de dados de clientes
    # Em produção, isso seria uma chamada para a API do MercadoPhone
    clients = [
        {
            "id": 1,
            "name": "João Silva",
            "email": "joao.silva@email.com",
            "phone": "(47) 99999-1111",
            "last_purchase": "2025-05-15",
            "total_purchases": 3,
            "total_value": 15000.00
        },
        {
            "id": 2,
            "name": "Maria Oliveira",
            "email": "maria.oliveira@email.com",
            "phone": "(47) 99999-2222",
            "last_purchase": "2025-06-01",
            "total_purchases": 1,
            "total_value": 8500.00
        },
        {
            "id": 3,
            "name": "Carlos Santos",
            "email": "carlos.santos@email.com",
            "phone": "(47) 99999-3333",
            "last_purchase": "2025-05-20",
            "total_purchases": 2,
            "total_value": 12000.00
        }
    ]
    
    return jsonify(clients), 200

@clients_bp.route("/<int:client_id>", methods=["GET"])
@jwt_required()
def get_client(client_id):
    """Rota para obter detalhes de um cliente específico."""
    # Simulação de dados de um cliente específico
    # Em produção, isso seria uma chamada para a API do MercadoPhone
    if client_id == 1:
        client = {
            "id": 1,
            "name": "João Silva",
            "email": "joao.silva@email.com",
            "phone": "(47) 99999-1111",
            "address": "Rua das Flores, 123 - Joinville, SC",
            "last_purchase": "2025-05-15",
            "total_purchases": 3,
            "total_value": 15000.00,
            "purchases": [
                {
                    "id": 101,
                    "date": "2025-05-15",
                    "products": ["MacBook Pro 16\"", "Apple Care+"],
                    "total": 25000.00
                },
                {
                    "id": 102,
                    "date": "2025-03-10",
                    "products": ["iPhone 15 Pro Max"],
                    "total": 12000.00
                },
                {
                    "id": 103,
                    "date": "2024-12-20",
                    "products": ["AirPods Pro 2"],
                    "total": 2500.00
                }
            ],
            "notes": "Cliente premium, sempre busca os últimos lançamentos. Prefere parcelamento em 12x."
        }
        return jsonify(client), 200
    else:
        return jsonify({"error": "Cliente não encontrado"}), 404

@clients_bp.route("/<int:client_id>/notes", methods=["POST"])
@jwt_required()
def update_client_notes(client_id):
    """Rota para atualizar anotações sobre um cliente."""
    # Obter dados da requisição
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Dados não fornecidos"}), 400
    
    notes = data.get("notes")
    
    if not notes:
        return jsonify({"error": "Anotações não fornecidas"}), 400
    
    # Em produção, isso seria uma atualização no banco de dados ou API do MercadoPhone
    # Simulação de sucesso
    return jsonify({
        "message": "Anotações atualizadas com sucesso",
        "client_id": client_id,
        "notes": notes
    }), 200

@clients_bp.route("/search", methods=["GET"])
@jwt_required()
def search_clients():
    """Rota para buscar clientes por nome, email ou telefone."""
    # Obter parâmetros da query
    query = request.args.get("q", "")
    
    if not query:
        return jsonify({"error": "Termo de busca não fornecido"}), 400
    
    # Simulação de resultados de busca
    # Em produção, isso seria uma busca no banco de dados ou API do MercadoPhone
    results = [
        {
            "id": 1,
            "name": "João Silva",
            "email": "joao.silva@email.com",
            "phone": "(47) 99999-1111",
            "last_purchase": "2025-05-15"
        }
    ]
    
    return jsonify(results), 200
