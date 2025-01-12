from flask import Flask
from auth import bp as auth_bp
from game import bp as game_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp)
    app.register_blueprint(game_bp)
    return app