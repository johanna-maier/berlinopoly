from datetime import datetime
from .. import db

class User(db.Model):
    """Users who play the game"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    icon = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # Relationships
    games = db.relationship('UserGame', back_populates="user")

    def __repr__(self):
        return f"<User {self.name}>"
