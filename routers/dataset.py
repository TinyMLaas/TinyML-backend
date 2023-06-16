from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session

from services import dataset_service
from schemas import schemas
from db.database import get_db

router = APIRouter()


@router.get("/datasets/", status_code=200, response_model=list[schemas.Dataset])
async def get_datasets(database: Session=Depends(get_db)):
    """Displays existing datasets
    """
    response = dataset_service.get_datasets(database)

    return response


@router.post("/datasets/", status_code=201,response_model=schemas.Dataset)
async def add_dataset(dataset_name, dataset_desc, database: Session=Depends(get_db)):
    """Adds a new dataset to the backend
    """

    return dataset_service.add_dataset(dataset_name, dataset_desc, database)


@router.post("/datasets/{dataset_id}/", status_code=200)
async def add_image_to_dataset(
    dataset_id, files: list[UploadFile],
    database: Session=Depends(get_db)):
    """Adds a new image to excisting dataset
    """

    return dataset_service.add_image_to_dataset(dataset_id,files ,database)
