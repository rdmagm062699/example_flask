from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()

@dataclass
class Data(db.Model):
    id: int
    data_value: str

    id = db.Column(db.Integer, primary_key=True)
    data_value = db.Column(db.String(150))

@dataclass
class OtherStuff(db.Model):
    id: int
    data_id: int
    column_one: str
    column_two: str

    id = db.Column(db.Integer, primary_key=True)
    data_id = db.Column(db.Integer, db.ForeignKey('data.id'), nullable=False)
    column_one = db.Column(db.String(150))
    column_two = db.Column(db.String(150))
    
