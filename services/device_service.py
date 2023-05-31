import os
import csv
import json
import pandas as pd

# New database features
from sqlalchemy.orm import Session
from schemas.device import DeviceCreate
from db.models import Device


# def create_device(db: Session, device: DeviceCreate):
#     db_device = models.Device(
#     id = device.id,
#     name = device.name,
#     connection = device.connection,
#     installer = device.installer,
#     compiler = device.compiler,
#     model = device.model,
#     description = device.description
#     )
#     db.add(db_device)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

def get_all_devices(database: Session, skip: int=0, limit: int=1000):
    result = database.query(Device).offset(skip).limit(limit).all()
    return result

def remove_device(database: Session, device_id: int, skip: int=0, limit: int=1000):
    device = database.query(Device).filter(Device.id == device_id).first()
    
    if device == None:
        raise ValueError()
    
    database.delete(device)
    database.commit()
    
    return None 

def add_device(database: Session, device: DeviceCreate, skip: int=0, limit: int=1000):
    """Add a new device to the software

    Args:
        device: the device to be added
    """

    db_device = Device(**device.dict())
    database.add(db_device)
    database.commit()
    database.refresh(db_device)
    
    return db_device
    

