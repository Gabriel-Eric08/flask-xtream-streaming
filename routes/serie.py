from flask import Flask, render_template, Blueprint, request, make_response, jsonify
import json, requests
from util.getcredentials import getCredentials

serie_route = Blueprint('Serie', __name__)

@serie_route.route('/<series_id>')
def serie(series_id):
    creds  = getCredentials()
    
    server = creds.get("URL_Xtream")
    user = creds.get("Username")
    password = creds.get("Password")

    url_get_serie = f"{server}/player_api.php?username={user}&password={password}&action=get_series_info&series_id={series_id}"

    try:

        response_serie = requests.get(url_get_serie)
        response_serie.raise_for_status()
        serie_info = response_serie.json()

        serie = {
                    "info": serie_info.get("info"),
                    "episodes": serie_info.get("episodes", {})
                }

        return render_template('serie.html', serie=serie)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500