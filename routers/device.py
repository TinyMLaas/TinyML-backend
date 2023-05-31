from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from services import device_service
from schemas.device import Device, DeviceCreate
from db.database import session


router = APIRouter()
sessionlocal = session()

def get_db():
    """Set up the database session for SQLAlchemy"""
    database = session()
    try:
        yield database
    finally:
        database.close()

@router.post("/add_device/", status_code=201)
async def add_device(device: DeviceCreate, database: Session=Depends(get_db)):
    """Adds a device"""
    try:
        response = device_service.add_device(database, device)
    except:
        raise HTTPException(status_code=422, detail="Insufficient device information.")
    return response


@router.get("/registered_devices/", response_model=list[Device])
async def list_registered_devices(database: Session=Depends(get_db)):
    """Displays registered devices"""
    response = device_service.get_all_devices(database)
    return response


@router.delete("/remove_device/{device_id}", status_code=204)
async def remove_registered_device(device_id, database: Session=Depends(get_db)):
    """Removes a device"""
    try:
        response = device_service.remove_device(database, device_id)
    except:
        raise HTTPException(status_code=400, detail="Unknown device id.")

    return response
