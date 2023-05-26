from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from services import device_service


router = APIRouter()


class Device(BaseModel):
    """The request body for device adding"""

    name: str = Field(min_length=1)
    connection: str | None = Field(default=None, min_length=1)
    installer: str | None = Field(default=None, min_length=1)
    compiler: str | None = Field(default=None, min_length=1)
    model: str = Field(min_length=1)
    description: str = Field(min_length=1)


class DeviceId(BaseModel):
    device_id: int


@router.post("/add_device/", status_code=201)
async def add_device(device: Device):
    """Adds a device"""
    device_service.add_device(device)


@router.get("/registered_devices/")
async def list_registered_devices():
    """Displays registered devices"""
    return device_service.get_registered_devices()


@router.delete("/remove_device/{device_id}")
async def remove_registered_device(device_id):
    """Removes a device"""
    try:
        response = device_service.remove_device(device_id)
    except:
        raise HTTPException(status_code=400, detail="Unknown device id.")

    return response
