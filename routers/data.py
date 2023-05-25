from fastapi import APIRouter
from services import data_service

router = APIRouter()


@router.get("/dataset_names")
async def get_dataset_names():
    return data_service.get_dataset_names()

@router.get("/dataset_names_size")
async def get_dataset_names_size():
    return data_service.get_dataset_names_size()