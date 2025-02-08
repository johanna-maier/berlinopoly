from datetime import datetime
from .. import db

class Game(db.Model):
    """Stores game sessions"""
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    finished_at = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.Enum('ongoing', 'complete', name="game_status"), nullable=False)
    winner_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    # Relationships
    users = db.relationship('UserGame', back_populates="game")

    def __repr__(self):
        return f"<Game {self.id} - {self.status}>"
