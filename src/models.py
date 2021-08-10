from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()

@dataclass
class Data(db.Model):
    def __init__(self, id, data_value):
        self.id = id
        self.data_value = data_value

    id: int
    data_value: str

    id = db.Column(db.Integer, primary_key=True)
    data_value = db.Column(db.String(50))
