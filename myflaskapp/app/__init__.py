#  Initializes Flask app and binds SQLAlchemy and Alembic together.
# double check with file structure
# set up blueprints for different models / app sections
# https://chatgpt.com/c/679fd857-eeec-800e-81d8-1b5ae9553c7d

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Load configurations (from config.py)
    app.config.from_object('instance.config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register routes and models
    from . import routes
    app.register_blueprint(routes.bp)

    return app
