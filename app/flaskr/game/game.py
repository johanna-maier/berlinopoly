
from flask import Blueprint, render_template, request, redirect, url_for
from db import get_db

bp = Blueprint('game', __name__,url_prefix='/game')

@bp.route('/start', methods=('GET', 'POST'))
def start_game():
    if request.method == 'POST':
        # Logic to save player names
        db = get_db()
        player1_name = request.form['player1']
        player2_name = request.form['player2']
        db.execute("INSERT INTO players (name) VALUES (?)", (player1_name,))
        db.execute("INSERT INTO players (name) VALUES (?)", (player2_name,))
        db.commit()
        return redirect(url_for('game.play'))  # or wherever to direct after starting a game
    return render_template('game/start.html')