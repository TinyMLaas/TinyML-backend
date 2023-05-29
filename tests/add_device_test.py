import unittest
from unittest import mock
from fastapi.testclient import TestClient
from main import app
import os
import json


@mock.patch.dict(os.environ,
                 {"DEVICE_FILENAME": "tests/device_test.csv"})
class AddDevice(unittest.TestCase):
    def setUp(self):
        rows = ["id,Device name,Connection,Installer,Compiler,Model,Description\n",
                "8,Espressif ESP-EYE,192.168.1.9,Arduino IDE,TFLiteConverter,  person_detection,\n",
                "9,Wio Terminal: ATSAMD51,192.168.1.11,Arduino IDE,TFLiteConverter,  person_detection,\n",
                "10,Himax WE-I Plus EVB Endpoint AI Development Board,192.168.1.11,Arduino IDE,TFLiteConverter,  person_detection,\n",
                "3,STM32F746 Discovery kit,192.168.1.4,Arduino IDE,TFLiteConverter, mnist_lstm,\n",
                "7,testataaaaa,192.168.1.8,Arduino IDE,TFLiteConverter,  person_detection,"]
        self.device_to_add = {
            "name": "Arduino",
            "connection": "192.168.1.10",
            "installer": "Arduino IDE",
            "compiler": "TFLiteConverter",
            "model": "Nano 33 BLE",
            "description": "An Arduino for modeling"
        }
        self.client = TestClient(app)
        self.filename = "tests/device_test.csv"
        with open(self.filename, "w", encoding="utf-8") as csv_file:
            for row in rows:
                csv_file.write(row)

    def tearDown(self):
        with open(self.filename, "w", encoding="utf-8"):
            pass

    def test_add_device_returns_200_with_correct_post(self):
        response = self.client.post(
            "/add_device/",
            json=self.device_to_add
        )
        assert response.status_code == 201

    def test_add_device_device_added_to_csv(self):
        self.client.post(
            "/add_device/",
            json=self.device_to_add
        )
        devices = {}
        with open('tests/device_test.csv', "r", encoding="utf-8") as csv_file:
            next(csv_file)
            for row in csv_file:
                row = row.strip()
                row = row.split(',')
                device = {
                    "name": row[1],
                    "connection": row[2],
                    "installer": row[3],
                    "compiler": row[4],
                    "model": row[5],
                    "description": row[6]
                }
                devices[int(row[0])] = device
        assert devices[0]["name"] == "Arduino"

    def test_return_error_if_correct_data_not_given(self):
        self.device_to_add["description"] = None
        response = self.client.post(
            "/add_device/",
            json=self.device_to_add
        )
        response.status_code == 422
        response = json.loads(response.text)
        assert response["detail"][0]["loc"][1] == "description"


if __name__ == '__main__':
    unittest.main()
