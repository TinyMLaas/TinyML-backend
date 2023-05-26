import os
import csv
import json
import pandas as pd
from pydantic import BaseModel, Field


class Device(BaseModel):
    name: str = Field(min_length=1)
    connection: str | None = Field(default=None, min_length=1)
    installer: str | None = Field(default=None, min_length=1)
    compiler: str | None = Field(default=None, min_length=1)
    model: str = Field(min_length=1)
    description: str = Field(min_length=1)


def get_max_id():
    """Get maximum id that exists in the current devices
    """

    df = pd.read_csv(os.environ["DEVICE_FILENAME"])
    return df["id"].astype(int).max() + 1


def add_device(device: Device):
    """Add a new device to the software

    Args:
        device: the device to be added
    """

    id = get_max_id()
    line = f"\n{id},{device.name}"
    types = [device.connection, device.installer,
             device.compiler, device.model, device.description]
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


def remove_device(device_id):
    device_id = int(device_id)

    df = pd.read_csv(os.environ["DEVICE_FILENAME"])

    if device_id in df["id"].values:
        df_filtered = df.loc[df["id"] != device_id]
        df_filtered.to_csv(os.environ["DEVICE_FILENAME"], index=False)
    else:
        raise ValueError()
