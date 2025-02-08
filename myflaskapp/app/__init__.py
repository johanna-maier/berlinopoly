from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Load configuration from environment variables
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models to ensure they are registered with SQLAlchemy
    from app.models import user
    from app.models import user_game
    from app.models import game
    from app.models import game_event_deck
    from app.models import game_property
    from app.models import field
    from app.models import event_card
    # Import other models here
    
    
    # Register Blueprints or other app components
    # from .views import main as main_blueprint
    # app.register_blueprint(main_blueprint)
    
    return app