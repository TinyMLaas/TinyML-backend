from sqlalchemy.orm import Session
from schemas import schemas
from db import models

import pandas as pd


# Reads dataset names from local csv-file
def get_dataset_names():
    dataset = pd.read_csv("./dataset.csv")
    dataset_names = dataset["Dataset_Name"]
    return {"dataset_names": dataset_names}

#Returns dataset names and size
def get_dataset_names_size():
    dataset = pd.read_csv("./dataset.csv")
    dataset_names = dataset["Dataset_Name"]
    dataset_size = dataset["Size"]
    response = []
    for name,size in zip(dataset_names, dataset_size):
        response.append({"name": name, "size":size},)
    return response


#Returns dataset images
def get_dataset_images(ds_id):
    return
    result =  database.select(models.Dataset).join(models.Images).filter(Images.id == Dataset.id)
    
