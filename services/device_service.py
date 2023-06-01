import os
import csv
import json
import pandas as pd

from sqlalchemy.orm import Session
from schemas import schemas
from db import models


def get_all_devices(database: Session, skip: int=0, limit: int=1000):
    result = database.query(models.Device).offset(skip).limit(limit).all()
    return result


def remove_device(database: Session, device_id: int, skip: int=0, limit: int=1000):
    device = database.query(models.Device).filter(models.Device.id == device_id).first()
    
    if device == None:
        raise KeyError()
    
    database.delete(device)
    database.commit()
    
    return None 


def add_device(database: Session, device: schemas.DeviceCreate, skip: int=0, limit: int=1000):
    """Add a new device to the software

    Args:
        device: the device to be added
    """

    db_device = models.Device(**device.dict())
    database.add(db_device)
    database.commit()
    database.refresh(db_device)
    
    return db_device
    

