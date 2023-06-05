from ipaddress import IPv4Address
from sqlalchemy.orm import Session
from schemas import schemas
from db import models


def get_all_bridges(database: Session):
    """Returns a list of all bridges in the database
    """

    result = database.query(models.Bridge).all()
    return result


def remove_bridge(database: Session, bridge_id: int):
    """Removes Bridge from database if it is there.
    """

    bridge = database.query(models.Bridge).filter(models.Bridge.id == bridge_id).first()

    if bridge is None:
        raise KeyError()

    database.delete(bridge)
    database.commit()


def add_bridge(database: Session, bridge: schemas.BridgeCreate):
    """Add a new Bridge to the software

    Args:
        bridge: the Bridge to be added
    """

    db_bridge = models.Bridge(ip_address=str(bridge.ip_address), name=bridge.name)
    database.add(db_bridge)
    database.commit()
    database.refresh(db_bridge)

    return db_bridge


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
