import unittest
from fastapi.testclient import TestClient
from main import app

from services import device_service
from routers import device


class GetDatasets(unittest.TestCase):
        
    def test_backend_returns_names_of_datasets(self):
        client = TestClient(app)
        response = client.get("/dataset_names/")
        self.assertIsNotNone(response.text)
        assert response.status_code == 200

    def test_backend_returns_names_and_size_of_datasets(self):
        client = TestClient(app)
        response = client.get("/dataset_names/")
        self.assertIsNotNone(response.text)
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()
