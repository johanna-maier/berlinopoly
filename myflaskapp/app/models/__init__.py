from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models here
from .user import User  # Import User model (or any other models)
from .event_card import EventCard
from .field import Field
from .game_event_deck import GameEventDeck
from .game_property import GameProperty
from .game import Game
from .user_game import UserGame

def init_db(app):
    """Initialize database with Flask app"""
    db.init_app(app)
