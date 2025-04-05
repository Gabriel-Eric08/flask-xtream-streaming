from flask import Flask, render_template, Blueprint, request, make_response, jsonify
import json, requests
from util.getcredentials import getCredentials

player_route = Blueprint('Player', __name__)

@player_route.route('/<id_filme>/<movie_name>')
def home(id_filme, movie_name):
    creds  = getCredentials()
    
    server = creds.get("URL_Xtream")
   
    user = creds.get("Username")
   
    password = creds.get("Password")
   
    playlistname = creds.get("Playlistname")
    
    movie_name1 = movie_name
    url_watch_movie = f"{server}/movie/{user}/{password}/{id_filme}.mp4"



    return render_template('player.html', movie_url=url_watch_movie, movie_name=movie_name1)