import requests
import json
import ipaddress
from sqlalchemy.orm import Session
from schemas import bridge as bridge_schema
from db import models


def get_all_bridges(database: Session):
    """Returns a list of all bridges in the database
    """

    result = database.query(models.Bridge).all()
    return result


def remove_bridge(database: Session, bridge_id: int):
    """Removes Bridge from database if it is there.
    """

    bridge = database.query(models.Bridge).filter(
        models.Bridge.id == bridge_id).first()

    if bridge is None:
        raise KeyError()

    database.delete(bridge)
    database.commit()


def add_bridge(database: Session, bridge: bridge_schema.BridgeCreate):
    """Add a new Bridge to the software

    Args:
        bridge: the Bridge to be added
    """

    db_bridge = models.Bridge(address=str(
        bridge.address), name=bridge.name, https=bridge.https)
    database.add(db_bridge)
    database.commit()
    database.refresh(db_bridge)

    return db_bridge


def get_a_bridge(database: Session, bridge_id: int):
    """Get a spesific bridge"""

    bridge = database.query(models.Bridge).filter(
        models.Bridge.id == bridge_id).one()
    return bridge


def get_address(address: str):
    try:
        ipaddress.ip_address(address)
        if "http://" not in address:
            address = "http://" + address
        address += ":5000"  # Later get port from database
    except ValueError:
        if "http://" not in address:
            address = "http://" + address
    return address


def get_devices(bridge_id: int, database: Session):
    """Send request to the bridge to get all connected devices
    """

    bridge = get_a_bridge(database, bridge_id)

    address = get_address(bridge.address) + "/devices"

    response = requests.get(address, timeout=(5, None))

    return json.loads(response.text)


def ping_bridge(bridge_id: int, database: Session):
    """Send request to bridge to see if it is up
    """

    bridge = get_a_bridge(database, bridge_id)

    address = get_address(bridge.address) + "/devices"

    try:
        response = requests.get(address, timeout=5)
        if response.status_code == 200:
            return {"online": True}
        raise requests.exceptions.ConnectionError()
    except requests.exceptions.ConnectionError:
        return {"online": False}
