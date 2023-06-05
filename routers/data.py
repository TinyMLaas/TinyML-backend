from fastapi import APIRouter
from services import data_service

router = APIRouter()

@router.get("/data/")
async def get_dataset_names_size():
    """Select a dataset"""
    return data_service.get_dataset_names_size()
