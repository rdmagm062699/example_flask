from src.models import Data
from flask import jsonify

def get_all(limit=None):
    all_data = Data.query.all()
    
    if limit == 'only_numbers':
        return [d for d in all_data if d.data_value.isnumeric()]
    else:
        return all_data

def add(db, data):
    new_data = Data()
    new_data.data_value = data['data_value']
    db.session.add(new_data)
    db.session.commit()
