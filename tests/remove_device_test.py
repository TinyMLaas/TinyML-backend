import unittest
from unittest import mock
from fastapi.testclient import TestClient
from main import app
import os
import json
import csv


@mock.patch.dict(os.environ,
                 {"DEVICE_FILENAME": "tests/device_test.csv"})
class RemoveDevice(unittest.TestCase):
    def setUp(self):
        rows = ["id,Device name,Connection,Installer,Compiler,Model,Description\n",
                "8,Espressif ESP-EYE,192.168.1.9,Arduino IDE,TFLiteConverter,  person_detection,\n",
                "9,Wio Terminal: ATSAMD51,192.168.1.11,Arduino IDE,TFLiteConverter,  person_detection,\n",
                "10,Himax WE-I Plus EVB Endpoint AI Development Board,192.168.1.11,Arduino IDE,TFLiteConverter,  person_detection,\n",
                "3,STM32F746 Discovery kit,192.168.1.4,Arduino IDE,TFLiteConverter, mnist_lstm,\n",
                "7,testataaaaa,192.168.1.8,Arduino IDE,TFLiteConverter,  person_detection,"]
        
        self.client = TestClient(app)
        self.filename = "tests/device_test.csv"
        with open(self.filename, "w", encoding="utf-8") as csv_file:
            for row in rows:
                csv_file.write(row)

    def tearDown(self):
        with open(self.filename, "w", encoding="utf-8"):
            pass

    def test_device_removed_succesfully(self):
        response = self.client.delete(
            "/remove_device/3"
        )
        
        with open(self.filename, "r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            
            for row in reader:
                assert "STM32F746" not in row
                
                
    def test_device_id_not_found_returns_error_code_400(self):
        response = self.client.delete(
            "/remove_device/999947382989324589164"
        )
        
        assert response.status_code == 400

if __name__ == '__main__':
    unittest.main()