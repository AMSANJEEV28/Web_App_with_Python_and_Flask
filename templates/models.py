from flask import Flask
from app import db

app = Flask(__name__)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)    

    def __repr__(self):
        return f'{self.title} created on {self.date}'

with app.app_context():
    db = SQLAlchemy(app)
    db.create_all()