import sqlite3
import os
import shutil
import unittest
import json
from fastapi.testclient import TestClient
from main import app

from tests.setup_tests import setup_database, teardown_database


class GetAllModels(unittest.TestCase):
    @classmethod
    def setup_class(self):
        setup_database()
        self.client = TestClient(app)

    def test_get_all_models(self):
        response = self.client.get("/models/")

        assert response.status_code == 200

        res = json.loads(response.text)

        self.assertEqual(1, len(res))
        self.assertEqual(list, type(res))

    @classmethod
    def teardown_class(self):
        teardown_database()


class TrainNewModel(unittest.TestCase):
    @classmethod
    def setup_class(self):
        setup_database()
        self.client = TestClient(app)

    def test_train_a_new_model(self):
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

        self.assertIsNotNone(response.text)
        assert response.status_code == 201

        self.assertIn("Detect people", response.text)

        res = json.loads(response.text)
        self.assertEqual(2, res["id"])

    def test_trained_model_in_directory(self):
        dir = os.listdir("test_models/")

        self.assertIn("2", dir)

    @classmethod
    def teardown_class(self):
        teardown_database()


class ContinueTrainingModel(unittest.TestCase):
    @classmethod
    def setup_class(self):
        setup_database()
        self.client = TestClient(app)

    def test_continuing_training_a_model(self):
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
        response = self.client.put(
            f"/models/2/datasets/2")
        self.assertIsNotNone(response.text)
        assert response.status_code == 200

        self.assertIn("Detect people", response.text)

        res = json.loads(response.text)
        self.assertEqual(2, res["id"])

    def test_trained_model_in_directory(self):
        dir = os.listdir("test_models/")

        self.assertIn("2", dir)

    @classmethod
    def teardown_class(self):
        teardown_database()



if __name__ == '__main__':
    unittest.main()
