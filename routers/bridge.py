from fastapi import APIRouter
from pydantic import BaseModel
from ipaddress import IPv4Address
from services import bridge_service

router = APIRouter()


class Bridge(BaseModel):
    ip_address: IPv4Address
    name: str | None = None


@router.post("/add_bridge/", status_code=201)
async def add_new_bridge(bridge: Bridge):
    bridge_service.add_bridge(bridge)