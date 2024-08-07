from app import db

# Employee model to store employee details #

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    hours_worked = db.relationship('Hour', backref='employee', lazy=True)
    