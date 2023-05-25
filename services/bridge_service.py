import os
import csv
import json
import pandas as pd
from ipaddress import IPv4Address
from pydantic import BaseModel


class Bridge(BaseModel):
    ip_address: IPv4Address
    name: str | None = None


def get_max_id():
    df = pd.read_csv(os.environ["BRIDGE_FILENAME"])
    if df.empty:
        return 1
    return df["id"].astype(int).max() + 1


def add_bridge(bridge: Bridge):
    bridge.ip_address = str(bridge.ip_address)
    if bridge.name is None:
        bridge.name = bridge.ip_address
    id = get_max_id()
    row = f"\n{id},{bridge.ip_address},{bridge.name}"
    with open(os.environ["BRIDGE_FILENAME"], 'a', encoding="utf-8") as csv:
        csv.write(row)


def get_registered_bridges():
    """Reads devices from a local csv file."""
    json_array = []

    with open(os.environ["BRIDGE_FILENAME"], "r", encoding="utf-8") as csv_file:
        csvReader = csv.DictReader(csv_file)

        for row in csvReader:
            json_array.append(row)

    json_string = json.dumps(json_array)

    return json_string
