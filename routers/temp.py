from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from services import device_service, observation_service
from schemas import schemas
from db.database import get_db


router = APIRouter()

@router.get("/test")
async def test(database: Session = Depends(get_db), bridge_id=3, device_id=5):
    res = observation_service.observe_device_on_bridge(database, bridge_id, device_id)
    return res
    