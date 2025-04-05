from flask import Flask, render_template, Blueprint, request, make_response, jsonify
import json, requests
from util.getcredentials import getCredentials

movies_route = Blueprint('Movies', __name__)

@movies_route.route('/<category_id>')
def movies(category_id):
    creds  = getCredentials()
    
    server = creds.get("URL_Xtream")
    user = creds.get("Username")
    password = creds.get("Password")

    url_get_movies = url_get_movies = f"{server}/player_api.php?username={user}&password={password}&action=get_vod_streams&category_id={category_id}"

    try:

        response_movies = requests.get(url_get_movies)
        response_movies.raise_for_status()
        movies_list = response_movies.json()



        return render_template('movies.html', movies=movies_list)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    
@movies_route.route('/')
def all_movies():
    creds  = getCredentials()
    
    server = creds.get("URL_Xtream")
    user = creds.get("Username")
    password = creds.get("Password")

    url_get_movies = url_get_movies = f"{server}/player_api.php?username={user}&password={password}&action=get_vod_streams"

    try:

        response_movies = requests.get(url_get_movies)
        response_movies.raise_for_status()
        movies_list = response_movies.json()

        

        return render_template('movies.html', movies=movies_list)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500