import os
import sqlite3
import shutil

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
                      ('2011-11-04', '2',
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
    if os.path.exists("test_compiled_models") & cleanup:
        shutil.rmtree("test_compiled_models")