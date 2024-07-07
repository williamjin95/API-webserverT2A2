from app import db

# Location model to store job location details #

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(200), nullable=False)
    jobs = db.relationship('Hour', backref='location', lazy=True)
