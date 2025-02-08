from .. import db

class EventCard(db.Model):
    """Stores all possible event cards"""
    __tablename__ = 'event_cards'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum('Positive', 'Negative', 'Neutral', name="event_type"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    balance_change = db.Column(db.Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f"<EventCard {self.title} - {self.type}>"
