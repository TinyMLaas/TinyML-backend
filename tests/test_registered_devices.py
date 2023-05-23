import unittest
from fastapi.testclient import TestClient
from main import app

from services import device_service
from routers import device


class GetDevices(unittest.TestCase):
        
    def test_backend_returns_list_of_registered_devices(self):
        client = TestClient(app)
        response = client.get("/registered_devices/")
        self.assertIsNotNone(response)
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()


    