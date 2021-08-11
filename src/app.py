import os
from flask import Flask, request, jsonify
from src.models import db, Data
from src.data import get_all, add

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
    limit = request.args.get('limit')
    return jsonify(get_all(limit))

@app.route('/data', methods=['POST'])
def blah():
    print(request.json)
    add(db, request.json)
    return "Data successfully added"
