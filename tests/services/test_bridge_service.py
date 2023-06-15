import unittest
from db.database import session
from services import bridge_service
from tests.setup_tests import setup_database, teardown_database


class BridgeService(unittest.TestCase):
    @classmethod
    def setup_class(self):
        setup_database()

    def test_getting_a_single_bridge_by_id(self):
        database = session()
        bridge = bridge_service.get_a_bridge(database=database, bridge_id=1)
        database.close()
        self.assertEqual(1, bridge.id)
        self.assertEqual(bridge.name, 'Coffee room')

    @classmethod
    def teardown_class(self):
        teardown_database()
