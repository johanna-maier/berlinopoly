import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://monopoly_user:monopoly_pass@localhost:8080/berlinopoly_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
