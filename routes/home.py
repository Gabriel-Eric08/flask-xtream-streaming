from flask import Flask, render_template, Blueprint, request, make_response, jsonify
import json, requests
from util.getcredentials import getCredentials

home_route = Blueprint('Home', __name__)

@home_route.route('/')
def home():
    creds  = getCredentials()
    
    server = creds.get("URL_Xtream")
    user = creds.get("Username")
    password = creds.get("Password")

    url_get_categories_movies = f"{server}/player_api.php?username={user}&password={password}&action=get_vod_categories"

    url_get_categories_series = f"{server}/player_api.php?username={user}&password={password}&action=get_series_categories"
    try:
        response_categories = requests.get(url_get_categories_movies)
        response_categories.raise_for_status()
        categories_movies_list = response_categories.json()

        response_series_categories = requests.get(url_get_categories_series)
        response_series_categories.raise_for_status()
        categories_series_list = response_series_categories.json()

        return render_template('home.html', categories_movies=categories_movies_list, categories_series=categories_series_list)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500