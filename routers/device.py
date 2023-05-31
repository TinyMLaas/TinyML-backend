from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from services import device_service
from schemas.device import Device, DeviceCreate
from db.database import SessionLocal, engine

router = APIRouter()

from pydantic import BaseModel, Field


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add_device/", status_code=201)
async def add_device(device: DeviceCreate):
    """Adds a device"""
    device_service.add_device(device)


# uses database
@router.get("/registered_devices/", response_model=list[Device])
async def list_registered_devices(db: Session=Depends(get_db)):
    """Displays registered devices"""
    devices = device_service.get_all_devices(db)
    return devices

# uses database
@router.delete("/remove_device/{device_id}", status_code=204)
async def remove_registered_device(device_id, db: Session=Depends(get_db)):
    """Removes a device"""
    try:
        response = device_service.remove_device(db, device_id)
    except:
        raise HTTPException(status_code=400, detail="Unknown device id.")
    
    return response


# @router.delete("/remove_device/{device_id}")
# async def remove_registered_device(device_id):
#     """Removes a device"""
#     try:
#         response = device_service.remove_device(device_id)
#     except:
#         raise HTTPException(status_code=400, detail="Unknown device id.")

#     return response
