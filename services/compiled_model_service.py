#dev mode
from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))


import os
from sqlalchemy.orm import Session
from TinyMLaaS_main.compiling import convert_model, convert_to_c_array, convert_model_to_cc
from services import model_service
from db import models


def compile_model(database: Session):
    # get dataset_id based on model_id
    # get dataset.path based on dataset_id
    # get model parameters: image_heigth, image_width, batch_size

    dataset_path = "./data/cars_dataset"
    model_path  ="./trained_model"

    compiled_model = convert_model(dataset_path=dataset_path, model_path=model_path)

from db import models

<<<<<<< HEAD
compile_model(None)
=======
def get_all_compiled_models(database: Session):
    """Returns a list of all compiled models in the database
    """
    result = database.query(models.CompiledModel).all()
    return result
>>>>>>> 68e81bbef7ba851f2ef44fe4e28bbb0f52b828d4
