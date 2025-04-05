from flask import Flask, render_template, Blueprint, request, make_response, jsonify
import json, requests
from util.getcredentials import getCredentials

series_route = Blueprint('Series', __name__)

@series_route.route('/<category_id>')
def series(category_id):
    creds  = getCredentials()
    
    server = creds.get("URL_Xtream")
    user = creds.get("Username")
    password = creds.get("Password")

    url_get_series = url_get_movies = f"{server}/player_api.php?username={user}&password={password}&action=get_series"

    try:

        response_series = requests.get(url_get_series)
        response_series.raise_for_status()
        all_series = response_series.json()
        series_list = [serie for serie in all_series if serie.get("category_id") == category_id]



        return render_template('series.html', series=series_list)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500