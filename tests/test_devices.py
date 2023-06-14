import sqlite3
import os
import unittest
from fastapi.testclient import TestClient
from main import app

from tests.setup_tests import setup_database, teardown_database


class RemoveDevice(unittest.TestCase):
    @classmethod
    def setup_class(self):
        setup_database()
        self.client = TestClient(app)

    def test_device_removed_succesfully(self):
        response = self.client.delete(
            "/devices/4"
        )

        assert response.status_code == 204

        check_removal = self.client.get(
            "/devices/"
        )

        self.assertNotIn("Commodore 64", check_removal.text)

    def test_device_id_not_found_returns_error_code_400(self):
        response = self.client.delete(
            "/devices/999947382989324589164"
        )

        assert response.status_code == 400

    @classmethod
    def teardown_class(self):
        teardown_database()


class GetAllDevices(unittest.TestCase):
    @classmethod
    def setup_class(self):
        setup_database()
        self.client = TestClient(app)

    def test_backend_returns_list_of_registered_devices(self):
        response = self.client.get("/devices/")
        self.assertIsNotNone(response.text)
        assert response.status_code == 200

    @classmethod
    def teardown_class(self):
        teardown_database()


class AddNewDevice(unittest.TestCase):
    @classmethod
    def setup_class(self):
        setup_database()
        self.client = TestClient(app)

        self.device_to_add = {
            "name": "Arduino",
            "connection": "192.168.1.10",
            "installer_id": "1",
            "model": "Nano 33 BLE",
            "description": "Now we test the adding ***!!!",
            "serial": "1234"
        }

    def test_device_is_added(self):
        response = self.client.post(
            "/devices/",
            json=self.device_to_add
        )
        assert response.status_code == 201

        check_added = self.client.get(
            "/devices/"
        )

        self.assertIn("Now we test the adding ***!!!", check_added.text)

    def test_return_error_if_incorrect_data_given(self):
        self.device_to_add["description"] = None
        response = self.client.post(
            "/devices/",
            json=self.device_to_add
        )

        assert response.status_code == 422

    @classmethod
    def teardown_class(self):
        teardown_database()


if __name__ == '__main__':
    unittest.main()
