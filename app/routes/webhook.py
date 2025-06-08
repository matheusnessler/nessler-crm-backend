from flask import Blueprint, request, jsonify

webhook_bp = Blueprint('webhook', __name__)

VERIFY_TOKEN = "nessler_istore_webhook_token"  # o mesmo usado no Facebook Developer

@webhook_bp.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return 'Token inválido', 403

    if request.method == 'POST':
        data = request.json
        print("Webhook recebido:", data)
        return jsonify(status="sucesso"), 200
