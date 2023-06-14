from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from services import installer_service
from schemas import schemas
from db.database import get_db


router = APIRouter()


@router.get("/installers/", status_code=200, response_model=list[schemas.Installer])
async def list_registered_installers(database: Session = Depends(get_db)):
    """Displays registered devices"""
    response = installer_service.get_all_installers(database)

    return response