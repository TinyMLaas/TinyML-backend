import csv
import json
import pandas as pd
from pydantic import BaseModel, Field
# from routers.device import Device


class Device(BaseModel):
    name: str = Field(min_length=1)
    connection: str | None = Field(default=None, min_length=1)
    installer: str | None = Field(default=None, min_length=1)
    compiler: str | None = Field(default=None, min_length=1)
    model: str = Field(min_length=1)
    description: str = Field(min_length=1)


def get_max_id():
    df = pd.read_csv("devices.csv")
    return df["id"].astype(int).max() + 1


def add_device(device: Device):
    id = get_max_id()
    line = f"\n{id},{device.name}"
    types = [device.connection, device.installer,
             device.compiler, device.model, device.description]
    for type in types:
        if type is not None:
            line += "," + type
        else:
            line += ",notgiven"
    with open("devices.csv", "a", encoding="utf-8") as csv_file:
        csv_file.write(line)


def get_registered_devices():
    json_array = []

    with open("devices.csv", "r", encoding="utf-8") as csv_file:
        csvReader = csv.DictReader(csv_file)

        for row in csvReader:
            json_array.append(row)

    json_string = json.dumps(json_array)

    return json_string
