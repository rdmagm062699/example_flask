import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

app = Flask(__name__)
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{db_user}:{db_password}@localhost/example'
db = SQLAlchemy(app)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/data')
def data():
    all_data = Data.query.all()
    return jsonify(all_data)

@app.route('/blah', methods=['POST'])
def blah():
    print(request.json)
    return ""

@dataclass
class Data(db.Model):
    id: int
    data_value: str

    id = db.Column(db.Integer, primary_key=True)
    data_value = db.Column(db.String(50))
