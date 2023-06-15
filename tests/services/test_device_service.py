import unittest
import db
from services import device_service
from tests.setup_tests import setup_database, teardown_database


class BridgeService(unittest.TestCase):
    @classmethod
    def setup_class(self):
        setup_database()

    def test_getting_a_single_bridge_by_id(self):
        database = db.database.session()
        device = device_service.get_a_device(database=database, device_id=1)
        database.close()
        self.assertEqual(type(device), db.models.Device)
        self.assertEqual(device.id, 1)
        self.assertEqual(device.name, 'Espressif ESP-EYE')

    @classmethod
    def teardown_class(self):
        teardown_database()
