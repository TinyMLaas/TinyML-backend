import json
from datetime import datetime
from sqlalchemy.orm import Session
# , convert_to_c_array, convert_model_to_cc
from TinyMLaaS_main.compiling import convert_model
from db import models
from schemas import schemas
from config import COMPILED_MODEL_DIR


def compile_model(database: Session, model_id: int):
    """Takes id of a trained model as parameter and compiles / converts it to
    a Tensorflow Lite model.
    """

    model = database.query(models.Model).filter(
        models.Model.id == model_id).first()
    dataset_path = model.dataset.path
    model_path = model.model_path
    model_params = json.loads(model.parameters.replace("'", '"'))

    now = datetime.now()

    db_model = schemas.CompiledModelCreate(
        created=now,
        compiler_id=None,
        model_id=model_id,
        model_path=model_path
    )

    db_model = save_compiled_model(db_model, database)

    convert_model(
        dataset_path=dataset_path,
        output_path=COMPILED_MODEL_DIR,
        model_path=model_path,
        model_params=model_params,
        model_name=str(db_model.id)
    )

    return db_model


def get_all_compiled_models(database: Session):
    """Returns a list of all compiled models in the database
    """

    result = database.query(models.CompiledModel).all()
    return result


def save_compiled_model(compiled_model: schemas.ModelCreate, database: Session):
    """Saves model to database
    """
    db_model = models.CompiledModel(**compiled_model.dict())
    database.add(db_model)
    database.commit()
    database.refresh(db_model)

    db_model.model_path = f"{COMPILED_MODEL_DIR}{db_model.id}"
    database.commit()
    database.refresh(db_model)

    return db_model


def get_compiled_model(compiled_model_id: int, database: Session):
    """Get the compiled model file
    """

    result = database.query(models.CompiledModel).filter(
        models.CompiledModel.id == compiled_model_id).one()
    path = result.model_path + "/model.cc"
    return path
