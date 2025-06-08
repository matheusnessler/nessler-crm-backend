"""
Rotas para o dashboard do CRM da Nessler iStore.
Versão otimizada para deploy no Render.
"""
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db

# Criar blueprint
dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/summary", methods=["GET"])
@jwt_required()
def get_summary():
    """Rota para obter resumo de dados para o dashboard."""
    # Simulação de dados para o dashboard
    # Em produção, isso seria uma agregação de dados do banco de dados ou API do MercadoPhone
    summary = {
        "total_clients": 156,
        "new_clients_month": 12,
        "total_sales_month": 185000.00,
        "average_ticket": 15416.67,
        "top_products": [
            {
                "name": "MacBook Pro 16\"",
                "sales": 5,
                "revenue": 125000.00
            },
            {
                "name": "iPhone 15 Pro Max",
                "sales": 8,
                "revenue": 96000.00
            },
            {
                "name": "iPad Pro 12.9\"",
                "sales": 3,
                "revenue": 45000.00
            }
        ],
        "sales_by_category": [
            {
                "category": "Notebooks",
                "sales": 8,
                "revenue": 180000.00
            },
            {
                "category": "Smartphones",
                "sales": 12,
                "revenue": 132000.00
            },
            {
                "category": "Tablets",
                "sales": 5,
                "revenue": 65000.00
            },
            {
                "category": "Smartwatches",
                "sales": 7,
                "revenue": 49000.00
            },
            {
                "category": "Acessórios",
                "sales": 15,
                "revenue": 30000.00
            }
        ]
    }
    
    return jsonify(summary), 200

@dashboard_bp.route("/sales-chart", methods=["GET"])
@jwt_required()
def get_sales_chart():
    """Rota para obter dados de vendas para gráficos."""
    # Simulação de dados para gráficos de vendas
    # Em produção, isso seria uma agregação de dados do banco de dados ou API do MercadoPhone
    sales_data = {
        "monthly": [
            {"month": "Janeiro", "sales": 150000.00},
            {"month": "Fevereiro", "sales": 180000.00},
            {"month": "Março", "sales": 165000.00},
            {"month": "Abril", "sales": 190000.00},
            {"month": "Maio", "sales": 210000.00},
            {"month": "Junho", "sales": 185000.00}
        ],
        "comparison": {
            "current_year": 1080000.00,
            "previous_year": 920000.00,
            "growth": 17.39
        }
    }
    
    return jsonify(sales_data), 200

@dashboard_bp.route("/recent-activities", methods=["GET"])
@jwt_required()
def get_recent_activities():
    """Rota para obter atividades recentes."""
    # Simulação de atividades recentes
    # Em produção, isso seria uma consulta ao banco de dados ou API do MercadoPhone
    activities = [
        {
            "id": 1,
            "type": "sale",
            "description": "Venda de MacBook Pro 16\" para João Silva",
            "value": 25000.00,
            "date": "2025-06-07T14:30:00Z"
        },
        {
            "id": 2,
            "type": "client",
            "description": "Novo cliente cadastrado: Maria Oliveira",
            "date": "2025-06-06T10:15:00Z"
        },
        {
            "id": 3,
            "type": "message",
            "description": "Mensagem de WhatsApp de Carlos Santos sobre iPad Pro",
            "date": "2025-06-05T16:45:00Z"
        },
        {
            "id": 4,
            "type": "sale",
            "description": "Venda de iPhone 15 Pro Max para Ana Pereira",
            "value": 12000.00,
            "date": "2025-06-05T11:20:00Z"
        },
        {
            "id": 5,
            "type": "stock",
            "description": "Atualização de estoque: +5 AirPods Pro 2",
            "date": "2025-06-04T09:00:00Z"
        }
    ]
    
    return jsonify(activities), 200
