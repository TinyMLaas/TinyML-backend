from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services import compiled_model_service
from db.database import get_db
from schemas.schemas import Model, CompiledModel

router = APIRouter()


@router.post("/compiled_models/models/{model_id}", status_code=201)
async def compile_model(database: Session = Depends(get_db)):
    """return training data"""

    response = compiled_model_service.compile()
    return response
