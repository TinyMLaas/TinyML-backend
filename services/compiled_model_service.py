import os
from sqlalchemy.orm import Session
from TinyMLaaS_main.compiling import convert_model, convert_to_c_array, convert_model_to_cc
from services import model_service
from db import models


def training(ds_id, training_data, lossfunc, database: Session):
    compiled_model = 
    return result

from db import models

def get_all_compiled_models(database: Session):
    """Returns a list of all compiled models in the database
    """
    result = database.query(models.CompiledModel).all()
    return result
