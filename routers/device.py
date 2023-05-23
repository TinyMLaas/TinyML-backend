from fastapi import APIRouter
from pydantic import BaseModel, Field
from services import device_service


class Device(BaseModel):
    name: str = Field(min_length=1)
    connection: str | None = Field(default=None, min_length=1)
    installer: str | None = Field(default=None, min_length=1)
    compiler: str | None = Field(default=None, min_length=1)
    model: str = Field(min_length=1)
    description: str = Field(min_length=1)


router = APIRouter()


@router.post("/add_device/")
async def add_device(device: Device):
    device_service.add_device(device)


@router.get("/registered_devices/")
async def list_registered_devices():
    return device_service.get_registered_devices()