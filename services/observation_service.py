import json
import requests
from sqlalchemy.orm import Session
from services import device_service, bridge_service


def observe_device_on_bridge(database: Session, bridge_id: int, device_id: int):
    """Call the wanted bridge to read the observations of a specified device on that bridge
    """

    device_serial = device_service.get_a_device(database=database, device_id=device_id).serial

    bridge_address = bridge_service.get_a_bridge(
         database, bridge_id
         ).ip_address

    data = {
        "device": {
            "serial": device_serial
        }
    }

    res = requests.get(
        f'http://{bridge_address}:5000/prediction/',
        json=data,
        timeout=(5, None)
        )

    return json.loads(res.text)
