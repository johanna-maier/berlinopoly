from .. import db

class Field(db.Model):
    """Tracks all game fields (streets, start, prison, event spaces)"""
    __tablename__ = 'fields'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.Enum('property', 'event', 'start', 'prison', name="field_type"), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=True)
    rent_base = db.Column(db.Numeric(10, 2), nullable=True)
    rent_with_house = db.Column(db.Numeric(10, 2), nullable=True)

    def __repr__(self):
        return f"<Field {self.name} - {self.type}>"
