from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services import device_service

router = APIRouter()

class DeviceId(BaseModel):
    device_id: int


@router.get("/registered_devices/")
async def list_registered_devices():
    return device_service.get_registered_devices()

@router.delete("/remove_device/{device_id}")
async def remove_registered_device(device_id):
    try:
        response = device_service.remove_device(device_id)    
    except:
        raise HTTPException(status_code=400, detail="Unknown device id.")
    
    return response
    
