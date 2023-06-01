from fastapi import APIRouter
from pydantic import BaseModel

from services import bridge_service
from schemas import schemas
from db.database import get_db


router = APIRouter()


@router.post("/add_bridge/", status_code=201)
async def add_new_bridge(bridge: schemas.BridgeCreate):
    bridge_service.add_bridge(bridge)


@router.get("/registered_bridges/")
async def registered_bridges():
    return bridge_service.get_registered_bridges()