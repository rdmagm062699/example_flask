import os
from flask import Flask, request, jsonify
from models import db, Data

app = Flask(__name__)
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{db_user}:{db_password}@localhost/example'
db.init_app(app)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/data')
def data():
    all_data = Data.query.all()
    return jsonify(all_data)

@app.route('/data', methods=['POST'])
def blah():
    print(request.json)
    return ""
