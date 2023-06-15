import unittest
import db
from services import compiled_model_service
from tests.setup_tests import setup_database, teardown_database


class BridgeService(unittest.TestCase):
    @classmethod
    def setup_class(self):
        setup_database()

    def test_getting_a_single_bridge_by_id(self):
        database = db.database.session()
        db_model = db.models.CompiledModel(**{
            'created': None,
            'model_id': 1,
            'model_path': 'test_compiled_models'
        })
        database.add(db_model)
        database.commit()
        path = compiled_model_service.get_compiled_model(
            compiled_model_id=1, database=database)
        database.close()
        self.assertEqual(type(path), str)
        self.assertEqual(path, 'test_compiled_models/model.cc')

    @classmethod
    def teardown_class(self):
        teardown_database()
