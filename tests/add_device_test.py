import unittest
from unittest import mock
from fastapi.testclient import TestClient
from main import app
import os


@mock.patch.dict(os.environ,
                 {"DEVICE_FILENAME": "tests/device_test.csv"})
class AddDevice(unittest.TestCase):
    def setUp(self):
        self.device_to_add = {
            "name": "Arduino",
            "connection": "192.168.1.10",
            "installer": "Arduino IDE",
            "compiler": "TFLiteConverter",
            "model": "Nano 33 BLE",
            "description": "An Arduino for modeling"
        }
        self.client = TestClient(app)

    def test_add_device_returns_200_with_correct_post(self):
        response = self.client.post(
            "/add_device/",
            json=self.device_to_add
        )
        assert response.status_code == 200

    def test_add_device_device_added_to_csv(self):
        _ = self.client.post(
            "/add_device",
            json=self.device_to_add
        )


if __name__ == '__main__':
    unittest.main()
