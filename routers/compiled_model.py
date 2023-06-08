from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas
from services import compiled_model_service
from db.database import get_db
from schemas import schemas

router = APIRouter()


@router.post("/compiled_models/models/{model_id}", status_code=201, response_model=schemas.CompiledModel)
async def compile_model(model_id, database: Session = Depends(get_db)):
    """return training data"""

    response = compiled_model_service.compile_model(database, model_id) # dev mode
    
    return response


@router.get("/compiled_models/", status_code=200, response_model=list[schemas.CompiledModel])
async def get_compiled_models(database: Session = Depends(get_db)):
    """Displays registered devices"""
    response = compiled_model_service.get_all_compiled_models(database)

    return response
