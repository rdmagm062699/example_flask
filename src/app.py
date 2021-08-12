import os
from flask import Flask, request, jsonify
from src.models import db, Data
from src.data_client import get_all_data, add_data, add_other_stuff

app = Flask(__name__)
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/example'
db.init_app(app)

@app.route('/v1')
def index():
  return 'Server Works!'
  
@app.route('/v1/data')
def get_data_route():
    limit = request.args.get('limit')
    return jsonify(get_all_data(limit))

@app.route('/v1/data', methods=['POST'])
def add_data_route():
    id = add_data(db, request.json)
    return { 'id': id }

@app.route('/v1/data/<int:data_id>/otherstuff', methods=['POST'])
def add_other_stuff_route(data_id):
    add_other_stuff(db, data_id, request.json)
    return ''