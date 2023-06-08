import sqlite3
import os
import shutil
import unittest
import json
from fastapi.testclient import TestClient
from main import app


cleanup = True


def setup_database():
    # remove excisting test database if there is one
    teardown_database()

    # create database file
    test_db = open("test_database.db", "w")
    test_db.close()

    # connect to test database
    con = sqlite3.connect("test_database.db")
    cur = con.cursor()

    # run sql schema from file
    with open("schema.sql", "r") as f:
        schema = f.read()

    # populate database
    with open("populate.sql") as f:
        populate = f.read()

    model_populate = """INSERT INTO
                      Models(created, dataset_id, parameters, description, model_path)
                      VALUES
                      ('2011-11-04T00:05:23Z', '2',
                      '{"epochs": 1, "img_width": 96, "img_height": 96, "batch_size": 1}',
                      'test_value','tensorflow_models/1')"""

    cur.executescript(schema)
    cur.executescript(populate)
    cur.executescript(model_populate)
    con.commit()
    con.close()


def teardown_database():
    if os.path.exists("test_database.db") & cleanup:
        os.remove("test_database.db")
    if os.path.exists("test_models/") & cleanup:
        shutil.rmtree("test_models/")


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


if __name__ == '__main__':
    unittest.main()
