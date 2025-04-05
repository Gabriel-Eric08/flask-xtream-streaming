from flask import Flask, render_template
from routes.auth import auth_route
from routes.home import home_route
from routes.player import player_route
from routes.movies import movies_route
app = Flask(__name__)




app.register_blueprint(home_route, url_prefix='/home')
app.register_blueprint(movies_route, url_prefix='/movies')
app.register_blueprint(player_route, url_prefix='/player')
app.register_blueprint(auth_route, url_prefix='/auth')


if __name__ == '__main__':
    app.run(debug=True)