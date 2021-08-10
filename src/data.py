from .models import Data
from flask import jsonify

def get_all():
    return Data.query.all()