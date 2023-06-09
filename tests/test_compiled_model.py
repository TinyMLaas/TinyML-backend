import sqlite3
import os
import shutil
import unittest
from unittest import mock
import json
from fastapi.testclient import TestClient
from main import app

from tests.setup_tests import setup_database, teardown_database

# Kouluta malli
# Testaa, että malli kääntyy x 2
# Tarkista, että get_all palauttaa listan jossa kaksi mallia


def mock_install_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.text = json_data
            self.status_code = status_code

    if args[0] == "http://192.168.0.7:5000/install/":
        if kwargs['json']['device']['serial'] != '707B266C064B14A6':
            print(kwargs['json']['device'])
            return MockResponse('Wrong device', 400)
        if len(kwargs['json']['model']) == 0:
            return MockResponse('No model', 400)
        return MockResponse('Success', 201)

    return MockResponse(None, 400)


class CompileNewModel(unittest.TestCase):
    @classmethod
    def setup_class(self):
        setup_database()
        self.client = TestClient(app)

        parameters = {
            "epochs": 1,
            "img_width": 96,
            "img_height": 96,
            "batch_size": 1
        }
        data = {
            "dataset_id": 2,
            "parameters": parameters,
            "description": "Detect people"
        }
        lossfunc = "Sparse Categorical crossentropy"
        response = self.client.post(
            f"/models/datasets/?lossfunc={lossfunc}",
            json=data
        )

        self.model_id = json.loads(response.text)["id"]

    def test_compile_a_new_model(self):

        compile_response = self.client.post(
            f"/compiled_models/models/{self.model_id}",
        )

        self.assertIsNotNone(compile_response.text)
        assert compile_response.status_code == 201

    @classmethod
    def teardown_class(self):
        teardown_database()

    def test_get_the_compiled_model(self):
        compile_response = self.client.get(
            "/compiled_models/1")
        assert compile_response.status_code == 200
        self.assertEqual('#include "target_model.h"',
                         compile_response.text.split('\n')[0])


class GetAllModels(unittest.TestCase):
    @classmethod
    def setup_class(self):
        setup_database()
        self.client = TestClient(app)

        parameters = {
            "epochs": 1,
            "img_width": 96,
            "img_height": 96,
            "batch_size": 1
        }
        data = {
            "dataset_id": 2,
            "parameters": parameters,
            "description": "Detect people"
        }
        lossfunc = "Sparse Categorical crossentropy"
        response = self.client.post(
            f"/models/datasets/?lossfunc={lossfunc}",
            json=data
        )

        self.model_id = json.loads(response.text)["id"]

        self.client.post(
            f"/compiled_models/models/{self.model_id}",
        )

        self.client.post(
            f"/compiled_models/models/{self.model_id}",
        )

    def test_get_all_compiled_models(self):
        response = self.client.get("/compiled_models/")

        assert response.status_code == 200

        res = json.loads(response.text)

        self.assertEqual(2, len(res))
        self.assertEqual(list, type(res))

    @mock.patch('services.compiled_model_service.requests.post', side_effect=mock_install_post)
    def test_install_compiled_model(self, mock_post):
        response = self.client.post("/compiled_models/1/bridges/1/devices/1")

        self.assertEqual(response.text, '"Success"')
        self.assertEqual(response.status_code, 201)

    @classmethod
    def teardown_class(self):
        teardown_database()


if __name__ == '__main__':
    unittest.main()
