from .. import db

class GameProperty(db.Model):
    """Tracks ownership and development of properties during a game"""
    __tablename__ = 'game_properties'

    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('fields.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    status = db.Column(db.Enum('free', 'purchased', 'house_built', name="property_status"), nullable=False)
    current_rent = db.Column(db.Numeric(10, 2), nullable=True)

    def __repr__(self):
        return f"<GameProperty {self.property_id} in Game {self.game_id}>"
