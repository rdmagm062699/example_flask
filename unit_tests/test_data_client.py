import flask_testing
from src.models import db, Data
from flask import Flask
from src.data_client import get_all_data, add_data


class TestDb(flask_testing.TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        return app

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_all_data_returns_empty_list_if_nothing_in_database(self):
        self.assertEqual(get_all_data(), [])

    def test_get_all_returns_all_database_data(self):
        test_data = [
            Data(id=1, data_value='blah'),
            Data(id=2, data_value='2'),
        ]

        db.session.bulk_save_objects(test_data)
        db.session.commit()

        expected = test_data
    
        self.assertEqual(get_all_data(), expected)

    def test_get_all_data_returns_only_numeric_values_if_instructed_to(self):
        test_data = [
            Data(id=1, data_value='blah'),
            Data(id=2, data_value='2'),
        ]

        db.session.bulk_save_objects(test_data)
        db.session.commit()

        expected = [Data(id=2, data_value='2')]
    
        self.assertEqual(get_all_data('only_numbers'), expected)

    def test_add_data_creates_specified_data(self):
        data = {
            'data_value': '123'
        }

        expected = [Data(id=1, data_value='123')]

        add_data(db, data)

        actual = Data.query.all()

        self.assertEqual(actual, expected)

    def test_add_data_returns_id_of_new_record(self):
        data = {
            'data_value': '123'
        }

        id = add_data(db, data)

        self.assertEqual(1, id)
