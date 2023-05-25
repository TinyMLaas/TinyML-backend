import os
from ipaddress import IPv4Address
from pydantic import BaseModel


class Bridge(BaseModel):
    ip_address: IPv4Address
    name: str | None = None


def add_bridge(bridge: Bridge):
    bridge.ip_address = str(bridge.ip_address)
    if bridge.name is None:
        bridge.name = bridge.ip_address
    row = f"\n{bridge.ip_address},{bridge.name}"
    with open(os.environ["BRIDGE_FILENAME"], 'a', encoding="utf-8") as csv:
        csv.write(row)
