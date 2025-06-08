"""
Rotas para gerenciamento de produtos no CRM da Nessler iStore.
Versão otimizada para deploy no Render.
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db

# Criar blueprint
products_bp = Blueprint("products", __name__)

@products_bp.route("/", methods=["GET"])
@jwt_required()
def get_products():
    """Rota para listar produtos do MercadoPhone."""
    # Simulação de dados de produtos
    # Em produção, isso seria uma chamada para a API do MercadoPhone
    products = [
        {
            "id": 1,
            "name": "MacBook Pro 16\"",
            "category": "Notebooks",
            "price": 25000.00,
            "stock": 5,
            "status": "available"
        },
        {
            "id": 2,
            "name": "iPhone 15 Pro Max",
            "category": "Smartphones",
            "price": 12000.00,
            "stock": 8,
            "status": "available"
        },
        {
            "id": 3,
            "name": "iPad Pro 12.9\"",
            "category": "Tablets",
            "price": 15000.00,
            "stock": 3,
            "status": "available"
        },
        {
            "id": 4,
            "name": "Apple Watch Ultra",
            "category": "Smartwatches",
            "price": 8000.00,
            "stock": 2,
            "status": "available"
        },
        {
            "id": 5,
            "name": "AirPods Pro 2",
            "category": "Acessórios",
            "price": 2500.00,
            "stock": 10,
            "status": "available"
        }
    ]
    
    return jsonify(products), 200

@products_bp.route("/<int:product_id>", methods=["GET"])
@jwt_required()
def get_product(product_id):
    """Rota para obter detalhes de um produto específico."""
    # Simulação de dados de um produto específico
    # Em produção, isso seria uma chamada para a API do MercadoPhone
    if product_id == 1:
        product = {
            "id": 1,
            "name": "MacBook Pro 16\"",
            "category": "Notebooks",
            "description": "MacBook Pro 16\" com chip M3 Pro, 32GB de RAM e 1TB de SSD",
            "price": 25000.00,
            "cost": 20000.00,
            "stock": 5,
            "status": "available",
            "specs": {
                "processor": "Apple M3 Pro",
                "memory": "32GB RAM",
                "storage": "1TB SSD",
                "display": "16\" Liquid Retina XDR",
                "color": "Space Black"
            },
            "sales_history": [
                {
                    "month": "Janeiro",
                    "quantity": 3,
                    "revenue": 75000.00
                },
                {
                    "month": "Fevereiro",
                    "quantity": 2,
                    "revenue": 50000.00
                },
                {
                    "month": "Março",
                    "quantity": 4,
                    "revenue": 100000.00
                }
            ]
        }
        return jsonify(product), 200
    else:
        return jsonify({"error": "Produto não encontrado"}), 404

@products_bp.route("/search", methods=["GET"])
@jwt_required()
def search_products():
    """Rota para buscar produtos por nome ou categoria."""
    # Obter parâmetros da query
    query = request.args.get("q", "")
    
    if not query:
        return jsonify({"error": "Termo de busca não fornecido"}), 400
    
    # Simulação de resultados de busca
    # Em produção, isso seria uma busca no banco de dados ou API do MercadoPhone
    results = [
        {
            "id": 1,
            "name": "MacBook Pro 16\"",
            "category": "Notebooks",
            "price": 25000.00,
            "stock": 5,
            "status": "available"
        }
    ]
    
    return jsonify(results), 200

@products_bp.route("/categories", methods=["GET"])
@jwt_required()
def get_categories():
    """Rota para listar categorias de produtos."""
    # Simulação de categorias
    # Em produção, isso seria uma busca no banco de dados ou API do MercadoPhone
    categories = [
        "Notebooks",
        "Smartphones",
        "Tablets",
        "Smartwatches",
        "Acessórios",
        "Desktops",
        "Monitores",
        "Áudio"
    ]
    
    return jsonify(categories), 200
