from src.models import Data, OtherStuff
from flask import jsonify

def get_all_data(limit=None):
    all_data = Data.query.all()
    
    if limit == 'only_numbers':
        return [d for d in all_data if d.data_value.isnumeric()]
    else:
        return all_data

def add_data(db, data):
    new_data = Data(data_value=data['data_value'])
    db.session.add(new_data)
    db.session.commit()
    db.session.flush()

    return new_data.id

def add_other_stuff(db, data_id, stuff):
    other_stuff = OtherStuff(data_id=data_id, column_one=stuff['column_one'], column_two=stuff['column_two'])
    db.session.add(other_stuff)
    db.session.commit()
