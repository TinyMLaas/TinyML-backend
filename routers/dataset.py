from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services import dataset_service
from schemas import schemas
from db.database import get_db

router = APIRouter()


@router.get("/datasets/", status_code=200, response_model=list[schemas.Dataset])
async def get_datasets(database: Session=Depends(get_db)):
    """Displays existing datasets"""
    response = dataset_service.get_datasets(database)
    return response