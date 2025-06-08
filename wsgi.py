"""
Ponto de entrada para a aplicação Flask do CRM Nessler iStore.
Versão otimizada para deploy no Render.
"""
from app import create_app

# Criar aplicação
app = create_app()

if __name__ == "__main__":
    # Usar porta fornecida pelo ambiente ou 5000 como padrão
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
