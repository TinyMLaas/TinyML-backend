from fastapi import APIRouter

from services import device_service

 
router = APIRouter()



@router.get("/registered_devices/")
async def list_registered_devices():
    return device_service.get_registered_devices()