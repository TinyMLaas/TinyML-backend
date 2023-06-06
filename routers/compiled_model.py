from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas
from services import compiled_model_service
from db.database import get_db
from schemas.schemas import Model, CompiledModel

router = APIRouter()


@router.post("/compiled_models/models/{model_id}", status_code=201)
async def compile_model(database: Session = Depends(get_db)):
    """return training data"""

    response = compiled_model_service.compile()
    return response

@router.get("/compiled_models/models/", status_code=200, response_model=list[schemas.CompiledModels])
async def list_registered_devices(database: Session = Depends(get_db)):
    """Displays registered devices"""
    response = device_service.get_all_devices(database)

    return response
