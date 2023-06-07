#dev mode
#from pathlib import Path
#import sys
#path_root = Path(__file__).parents[1]
#sys.path.append(str(path_root))
# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from services import model_service
# from db.database import get_db
# from schemas import schemas


import os
from sqlalchemy.orm import Session
from TinyMLaaS_main.compiling import convert_model, convert_to_c_array, convert_model_to_cc
from services import model_service
from db import models


def compile_model(database: Session, model_id: int):
    #here we should use relationships...
    # get dataset_id based on model_id
    model = database.query(models.Model).filter(models.Model.id == model_id).first()
    dataset_path = model.dataset.path
    model_path = model.model_path
    model_params = model.parameters

    # get dataset.path based on dataset_id
    # dataset = database.query(models.Dataset).filter(models.Dataset.id == dataset_id).first()
    # dataset_path = dataset.path

    # print("Dataset path for model =", dataset_path)

    # get model parameters: image_heigth, image_width, batch_size
    print("Model path:", model_path)
    compiled_model = convert_model(dataset_path=dataset_path, model_path=model_path, model_params=model_params)


    compiled_model = convert_model(dataset_path=dataset_path, model_path=model_path)

def get_all_compiled_models(database: Session):
    """Returns a list of all compiled models in the database
    """
    result = database.query(models.CompiledModel).all()
    return result
