import flask_testing
from src.models import db, Data, OtherStuff
from flask import Flask
from src.data_client import get_all_data, add_data, add_other_stuff, get_other_stuff


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

    def test_add_other_stuff_add_specfied_data(self):
        data = {
            'data_value': '123'
        }

        data_id = add_data(db, data)

        other_stuff = {
            'column_one': '1',
            'column_two': '2'
        }

        expected = [OtherStuff(id=1, data_id=data_id, column_one='1', column_two='2')]

        add_other_stuff(db, data_id, other_stuff)

        actual = OtherStuff.query.all()

        self.assertEqual(actual, expected)

    def test_get_other_stuff_returns_expected_data(self):
        test_data = [
            Data(id=1, data_value='blah')
        ]

        db.session.bulk_save_objects(test_data)

        test_other_stuff = [
            OtherStuff(data_id=1, column_one='blah1', column_two='blahblah1')
        ]

        db.session.bulk_save_objects(test_other_stuff)
        db.session.commit()

        expected = [
            OtherStuff(id=1, data_id=1, column_one='blah1', column_two='blahblah1')
        ]

        actual = get_other_stuff(1)

        self.assertEqual(actual, expected);

    def test_get_other_stuff_returns_expected_data_for_specified_data_id(self):
        test_data = [
            Data(id=1, data_value='blah'),
            Data(id=2, data_value='blah')
        ]

        db.session.bulk_save_objects(test_data)

        test_other_stuff = [
            OtherStuff(data_id=1, column_one='blah1', column_two='blahblah1'),
            OtherStuff(data_id=2, column_one='blah2', column_two='blahblah2')
        ]

        db.session.bulk_save_objects(test_other_stuff)
        db.session.commit()

        request_data_id = 2

        expected = [
            OtherStuff(id=2, data_id=2, column_one='blah2', column_two='blahblah2')
        ]

        actual = get_other_stuff(request_data_id)

        self.assertEqual(actual, expected)
