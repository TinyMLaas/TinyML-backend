from pydantic import BaseModel, Field
from pydantic.types import Optional


class InstallerBase(BaseModel):
    """Base for Installer model. Lacks id as it is assigned by database.
    """
    name: str = Field(min_length=1)


class Installer(InstallerBase):
    """If Installer is in database, it always has an id.
    """
    id: int

    class Config:
        orm_mode = True