from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from services import bridge_service
from schemas import schemas
from db.database import get_db


router = APIRouter()


@router.post("/bridges/", status_code=201, response_model=schemas.Bridge)
async def add_bridge(bridge: schemas.BridgeCreate, database: Session = Depends(get_db)):
    """Adds a bridge."""
    try:
        response = bridge_service.add_bridge(database, bridge)
    except Exception as exc:
        raise HTTPException(
            status_code=422, detail="Insufficient bridge information.") from exc

    return response


@router.get("/bridges/", status_code=200, response_model=list[schemas.Bridge])
async def get_registered_bridges(database: Session = Depends(get_db)):
    """Displays registered Bridges"""
    response = bridge_service.get_all_bridges(database)

    return response


@router.delete("/bridges/{bridge_id}", status_code=204)
async def remove_registered_bridge(bridge_id, database: Session = Depends(get_db)):
    """Removes a Bridge"""
    try:
        bridge_service.remove_bridge(database, bridge_id)
    except Exception as exc:
        raise HTTPException(
            status_code=400, detail="Unknown bridge id.") from exc
