import json
from datetime import datetime
import requests
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
# , convert_to_c_array, convert_model_to_cc
from TinyMLaaS_main.compiling import convert_model
from db import models
from schemas import compiled_model as compiled_model_schema
from schemas import model as model_schema
from config import COMPILED_MODEL_DIR
from services import bridge_service, device_service


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

    db_model = compiled_model_schema.CompiledModelCreate(
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


def save_compiled_model(compiled_model: model_schema.ModelCreate, database: Session):
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
    path = result.model_path + "/target_model.cc"
    return path


def install_to_device(compiled_model_id: int, bridge_id: int, device_id: int, database: Session):
    """Call the wanted bridge to install the wanted compiled model on the wanted device
    """

    model_path = get_compiled_model(compiled_model_id, database)
    with open(model_path, "r") as file:
        cmodel = file.read()
    bridge_address = bridge_service.get_a_bridge(
        database, bridge_id).ip_address
    device = device_service.get_a_device(database, device_id)
    serial, installer = device.serial, device.installer.name

    data = {
        "device": {
            "installer": installer,
            "serial": serial
        },
        "model": str(cmodel)
    }
    res = requests.post(
        f'http://{bridge_address}:5000/install/', json=data, timeout=(5, None))

    if res.status_code != 201:
        raise HTTPException(status_code=res.status_code, detail=res.text)

    return res.text
