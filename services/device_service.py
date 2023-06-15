from sqlalchemy.orm import Session

from db import models
from schemas import schemas


def get_all_devices(database: Session):
    """Returns a list of all devices in the database
    """

    result = database.query(models.Device).all()

    return result


def remove_device(database: Session, device_id: int):
    """Removes device from database if it is there.
    """

    device = database.query(models.Device).filter(
        models.Device.id == device_id).first()

    if device is None:
        raise KeyError()

    database.delete(device)
    database.commit()


def add_device(database: Session, device: schemas.DeviceCreate):
    """Add a new device to the software

    Args:
        device: the device to be added
    """

    db_device = models.Device(**device.dict())
    database.add(db_device)
    database.commit()
    database.refresh(db_device)

    return db_device


def get_a_device(database: Session, device_id: int):
    """Get a spesific device based on device id"""

    device = database.query(models.Device).filter(
        models.Device.id == device_id).one()
    return device
