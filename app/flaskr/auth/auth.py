from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash
from db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        # Process form data here
        # If successful:
        flash('Registration successful! Please log in.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')
   
    

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        # Authenticate user here
        # If successful:
        # session['user_id'] = user['id']  # Assuming you have user info
        return redirect(url_for('game.start_game'))  # Redirect to game start
    return render_template('auth/login.html')