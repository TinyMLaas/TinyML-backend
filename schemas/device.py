from pydantic import BaseModel, Field
from pydantic.types import Optional

from schemas.installer import Installer
from schemas.bridge import Bridge


class DeviceBase(BaseModel):
    """Base for Device model. Lacks id as it is assigned by database.
    """
    name: str = Field(min_length=1)
    connection: str | None = Field(default=None, min_length=1)
    installer_id: int
    model: str = Field(min_length=1)
    description: str = Field(min_length=1)
    serial:  str = Field(min_length=1)


class Device(DeviceBase):
    """If Device is in database, it always has an id.
    """
    id: int
    installer: Optional[Installer] = None
    bridge: Optional[Bridge] = None

    class Config:
        orm_mode = True


class DeviceCreate(DeviceBase):
    """When creating a new Device, there is yet no id.
    """

    class Config:
        orm_mode = True

