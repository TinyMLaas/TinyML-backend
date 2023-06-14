from db import models
from schemas import schemas
from sqlalchemy.orm import Session



def get_all_installers(database: Session):
    """Returns a list of all installers in the database
    """

    result = database.query(models.Installer).all()
    
    return result
