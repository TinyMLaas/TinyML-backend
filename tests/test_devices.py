import sqlite3
import os
import unittest
from fastapi.testclient import TestClient
from main import app

import routers.device

cleanup = True

def setup_database():
    #teardown_database()
    
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

    cur.execute(schema)
    cur.execute(populate)
    con.commit()
    con.close()

def teardown_database():
    if os.path.exists("test_database.db") & cleanup:
        os.remove("test_database.db")


class RemoveDevice(unittest.TestCase):
    @classmethod
    def setup_class(self):        
        setup_database()
        self.client = TestClient(app)


    @classmethod  
    def teardown_class(self):
        teardown_database()
            
    def test_device_removed_succesfully(self):
        response = self.client.delete(
            "/remove_device/4"
        )
        
        assert response.status_code == 204
        
        check_removal = self.client.get(
            "/registered_devices/"
        )
        
        self.assertNotIn("Commodore 64", check_removal.text)  
        
                    
    def test_device_id_not_found_returns_error_code_400(self):
        response = self.client.delete(
            "/remove_device/999947382989324589164"
        )
        
        assert response.status_code == 400


class GetAllDevices(unittest.TestCase):
    @classmethod
    def setup_class(self):        
        setup_database()
        self.client = TestClient(app)


    @classmethod  
    def teardown_class(self):
        teardown_database()
            
    
    def test_backend_returns_list_of_registered_devices(self):
        response = self.client.get("/registered_devices/")
        self.assertIsNotNone(response.text)
        assert response.status_code == 200
    
    



if __name__ == '__main__':
    unittest.main()