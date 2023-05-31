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

def get_all_devices(db: Session, skip: int=0, limit: int=1000):
    result = db.query(Device).offset(skip).limit(limit).all()
    return result

def remove_device(db: Session, device_id: int, skip: int=0, limit: int=1000):
    device = db.query(Device).filter(Device.id == device_id).first()
    
    if device == None:
        raise ValueError()
    
    db.delete(device)
    db.commit()
    
    return None 

#Old features, we'll migrate these
def get_max_id():
    """Get maximum id that exists in the current devices"""

    df = pd.read_csv(os.environ["DEVICE_FILENAME"])
    ids = df["id"].to_list()
    unique = set()
    biggest = 0
    for id in ids:
        biggest = max(biggest, id)
        unique.add(id)
    for i in range(biggest+1):
        if i not in unique:
            return iprint("service says:", device_id)
    return biggest + 1


def add_device(device: DeviceCreate):
    """Add a new device to the software

    Args:
        device: the device to be added
    """

    id = get_max_id()
    line = f"\n{id},{device.name}"
    types = [
        device.connection,
        device.installer,
        device.compiler,
        device.model,
        device.description,
    ]
    for type in types:
        if type is not None:
            line += "," + type
        else:
            line += ",notgiven"
    with open(os.environ["DEVICE_FILENAME"], "a", encoding="utf-8") as csv_file:
        csv_file.write(line)


def get_registered_devices():
    """Reads devices from a local csv file."""
    json_array = []

    with open(os.environ["DEVICE_FILENAME"], "r", encoding="utf-8") as csv_file:
        csvReader = csv.DictReader(csv_file)

        for row in csvReader:
            json_array.append(row)

    json_string = json.dumps(json_array)

    return json_string



# def remove_device(device_id):
#     device_id = int(device_id)

#     df = pd.read_csv(os.environ["DEVICE_FILENAME"])

#     if device_id in df["id"].values:
#         df_filtered = df.loc[df["id"] != device_id]
#         df_filtered.to_csv(os.environ["DEVICE_FILENAME"], index=False)
#     else:
#         raise ValueError()
