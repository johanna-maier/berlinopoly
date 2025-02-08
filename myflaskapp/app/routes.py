# app/routes.py

from flask import Blueprint, render_template, request
from .models import User  # import your models here
from . import db

# Define the blueprint
bp = Blueprint('main', __name__)

# Define your routes
@bp.route('/')
def index():
    return "Welcome to Berlinopoly!"

# @bp.route('/users')
# def show_users():
#     # Fetch all users from the database
#     users = User.query.all()  # Assuming you have a User model
#     return render_template('users.html', users=users)

# @bp.route('/add_user', methods=['POST'])
# def add_user():
#     name = request.form['name']
#     email = request.form['email']
#     user = User(name=name, email=email)
#     db.session.add(user)
#     db.session.commit()
#     return "User added successfully!"
