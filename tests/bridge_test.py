import unittest
import os
from unittest import mock
from fastapi.testclient import TestClient
from main import app


@mock.patch.dict(os.environ,
                 {"BRIDGE_FILENAME": "tests/bridge_test.csv"})
class Bridge(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.filename = "tests/bridge_test.csv"
        self.data = {
            "ip_address": '127.0.0.1',
            "name": "bridge"
        }
        row = "id,address,name"
        with open(self.filename, "w", encoding="utf-8") as csv:
            csv.write(row)

    def tearDown(self):
        with open(self.filename, "w", encoding="utf-8"):
            pass

    def test_add_bridge_to_csv(self):
        response = self.client.post(
            "/add_bridge/",
            json=self.data
        )
        assert response.status_code == 201

    def test_bridge_added_to_csv(self):
        self.client.post(
            "/add_bridge/",
            json=self.data
        )
        bridges = {}
        with open(self.filename, "r", encoding="utf-8") as csv:
            next(csv)
            for row in csv:
                bridges[row[0]] = {"address": "".join(row[2:11]), "name": row[12]}
        assert len(bridges) == 1
        assert bridges['1']["address"] == "127.0.0.1"

    def test_registered_bridges(self):
        pass


if __name__ == "__main__":
    unittest.main()