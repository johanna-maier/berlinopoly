from .. import db

class UserGame(db.Model):
    """Tracks user participation and stats for each game"""
    __tablename__ = 'users_games'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    current_balance = db.Column(db.Numeric(10, 2), nullable=False)
    current_position = db.Column(db.String(255), nullable=False)
    next_player = db.Column(db.Boolean, nullable=False, default=False)

    # Relationships
    user = db.relationship("User", back_populates="games")
    game = db.relationship("Game", back_populates="users")

    def __repr__(self):
        return f"<UserGame {self.user_id} in Game {self.game_id}>"
