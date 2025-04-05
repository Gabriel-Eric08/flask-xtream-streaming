from flask import Flask, render_template, Blueprint, request, make_response, jsonify, redirect, url_for
import json
import requests

auth_route = Blueprint('Auth', __name__)

@auth_route.route('/')
def home():
    return render_template('index.html')

@auth_route.route('/', methods=['POST'])
def auth():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Credenciais não encontradas!'}), 400
        
    try:
        url = f"{data['URL_Xtream']}/player_api.php?username={data['Username']}&password={data['Password']}"
        response = requests.get(url)

        if response.status_code == 200:
            response_data = response.json()

            if response_data.get("user_info", {}).get("status") == "Active":
                resp = make_response(jsonify({
                    'message': 'Credenciais registradas com sucesso!','redirect': url_for('Home.home')}))
                resp.set_cookie('Credentials', json.dumps(data))
                return resp
                
            else:
                return jsonify({'error': 'Falha na autenticação'}), 401
        else:
            return jsonify({'error': 'Erro na autenticação, resposta do servidor não foi 200'}), 401
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
