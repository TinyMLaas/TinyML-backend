import sqlite3
import os
import unittest
from fastapi.testclient import TestClient
from main import app

from tests.setup_tests import setup_database, teardown_database


class GetAllBridges(unittest.TestCase):
    @classmethod
    def setup_class(self):        
        setup_database()
        self.client = TestClient(app)


    def test_backend_returns_list_of_dataset(self):
        response = self.client.get(
            "/datasets/"
        )
        
        self.assertIsNotNone(response.text)
        assert response.status_code == 200


    @classmethod  
    def teardown_class(self):
        teardown_database()


if __name__ == '__main__':
    unittest.main()
