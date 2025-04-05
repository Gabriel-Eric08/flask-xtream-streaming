from flask import Flask, render_template, request, make_response, jsonify
import json
import requests



def getCredentials():
    data = request.cookies.get('Credentials')

    if not data:
        return jsonify({"error": "Credenciais não encontradas!"}), 404

    try:
        creds = json.loads(data)
        return creds
    except json.JSONDecodeError:
        return jsonify({"error": "Formato de credenciais inválido!"}), 400
