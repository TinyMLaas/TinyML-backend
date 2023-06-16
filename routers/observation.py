from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services import observation_service
from schemas import schemas
from db.database import get_db


router = APIRouter()


@router.get(
    "/observations/bridges/{bridge_id}/devices/{device_id}", 
    status_code=200,
    response_model=schemas.Observation)
async def observe_device_on_bridge(
    bridge_id: int,
    device_id: int,
    database: Session = Depends(get_db)):
    """Requests a single observation from a specified device on a specified bridge.
    """
    observation = observation_service.observe_device_on_bridge(database, bridge_id, device_id)

    response = schemas.Observation(
        bridge_id = bridge_id,
        device_id = device_id,
        observation_value = observation)

    return response
