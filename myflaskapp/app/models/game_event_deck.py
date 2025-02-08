from .. import db

class GameEventDeck(db.Model):
    """Tracks event card queue for each game"""
    __tablename__ = 'game_event_decks'

    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    event_card_id = db.Column(db.Integer, db.ForeignKey('event_cards.id'), nullable=False)
    position_in_queue = db.Column(db.Integer, nullable=False)
    is_drawn = db.Column(db.Boolean, default=False)
    drawn_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<GameEventDeck Game {self.game_id} Card {self.event_card_id}>"
