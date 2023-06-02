from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from services import device_service
from schemas import schemas
from db.database import get_db


router = APIRouter()


@router.post("/devices/", status_code=201, response_model=schemas.Device)
async def add_device(device: schemas.DeviceCreate, database: Session=Depends(get_db)):
    """Adds a device"""
    try:
        response = device_service.add_device(database, device)
    except Exception as exc:
        raise HTTPException(status_code=422, detail="Insufficient device information.") from exc

    return response


@router.get("/devices/", status_code=200, response_model=list[schemas.Device])
async def list_registered_devices(database: Session=Depends(get_db)):
    """Displays registered devices"""
    response = device_service.get_all_devices(database)

    return response


@router.delete("/devices/{device_id}", status_code=204)
async def remove_registered_device(device_id, database: Session=Depends(get_db)):
    """Removes a device"""
    try:
        device_service.remove_device(database, device_id)
    except Exception as exc:
        raise HTTPException(status_code=400, detail="Unknown device id.") from exc
