from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import schemas
from services import compiled_model_service
from db.database import get_db
from schemas import schemas

router = APIRouter()


@router.post(
    "/compiled_models/models/{model_id}",
    status_code=201,
    response_model=schemas.CompiledModel
)
async def compile_model(model_id, database: Session = Depends(get_db)):
    """Compile an existing model"""

    response = compiled_model_service.compile_model(database, model_id)

    return response


@router.get(
    "/compiled_models/",
    status_code=200,
    response_model=list[schemas.CompiledModel]
)
async def get_compiled_models(database: Session = Depends(get_db)):
    """Display compiled models"""
    response = compiled_model_service.get_all_compiled_models(database)

    return response


@router.get(
    "/compiled_models/{compiled_model_id}",
    status_code=200
)
async def get_compiled_model(compiled_model_id, database: Session = Depends(get_db)):
    """Get the compiled model.

    This returns the compiled cc array file.
    """

    path = compiled_model_service.get_compiled_model(
        compiled_model_id, database)

    return FileResponse(path, filename="model.cc")


@router.post(
    "/compiled_models/{compiled_model_id}/bridges/{bridge_id}/devices/{device_id}", status_code=200
)
async def install_model_to_device_on_brdige(compiled_model_id, bridge_id,
                                            device_id, database: Session = Depends(get_db)):
    """Installs selected compiled model on a specified device connected to a specified bridge
    """
    res = compiled_model_service.install_to_device(
        compiled_model_id, bridge_id, device_id, database)
    
    return res
