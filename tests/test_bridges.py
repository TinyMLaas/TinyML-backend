import sqlite3
import os
import unittest
from fastapi.testclient import TestClient
from main import app

from tests.setup_tests import setup_database, teardown_database


class RemoveBridge(unittest.TestCase):
    @classmethod
    def setup_class(self):        
        setup_database()
        self.client = TestClient(app)

            
    def test_bridge_removed_succesfully(self):
        response = self.client.delete(
            "/bridges/2"
        )
        
        assert response.status_code == 204
        
        check_removal = self.client.get(
            "/bridges/"
        )
        
        self.assertNotIn("Parking lot", check_removal.text)  
        
                    
    def test_bridge_id_not_found_returns_error_code_400(self):
        response = self.client.delete(
            "/bridges/999947382989324589164"
        )
        
        assert response.status_code == 400

    @classmethod  
    def teardown_class(self):
        teardown_database()


class GetAllBridges(unittest.TestCase):
    @classmethod
    def setup_class(self):        
        setup_database()
        self.client = TestClient(app)

    def test_backend_returns_list_of_registered_bridges(self):
        response = self.client.get(
            "/bridges/"
        )
        
        self.assertIsNotNone(response.text)
        assert response.status_code == 200

    @classmethod  
    def teardown_class(self):
        teardown_database()
            
    
class AddNewBridges(unittest.TestCase):
    @classmethod
    def setup_class(self):        
        setup_database()
        self.client = TestClient(app)
        
        self.bridge_to_add = {
            "ip_address": "0.0.0.0",
            "name": "Garage and mancave",
        }


    def test_bridge_is_added(self):
        response = self.client.post(
            "/bridges/",
            json=self.bridge_to_add
        )
        assert response.status_code == 201
        
        check_added = self.client.get(
            "/bridges/"
        )
        
        self.assertIn("Garage and mancave", check_added.text) 
        
        
    def test_return_error_if_incorrect_data_given(self):
        self.bridge_to_add["ip_address"] = None
        response = self.client.post(
            "/bridges/",
            json=self.bridge_to_add
        )
        
        assert response.status_code == 422
    
    
    @classmethod  
    def teardown_class(self):
        teardown_database()        



if __name__ == '__main__':
    unittest.main()