from pydantic import BaseModel
from pydantic.types import Optional


class BridgeBase(BaseModel):
    """Base for Bridge model. Lacks id as it is assigned by database.
    """
    address: str
    name: str | None = None
    https: bool


class Bridge(BridgeBase):
    """If Bridge is in database, it always has an id.
    """
    id: int

    class Config:
        orm_mode = True


class BridgeCreate(BridgeBase):
    """When creating a new Bridge, there is yet no id.
    """

    class Config:
        orm_mode = True


class BridgeDevice(BaseModel):
    manufacturer: str
    product: str
    serial: str


class BridgeDevices(BaseModel):
    devices: list[BridgeDevice]


class BridgeStatus(BaseModel):
    online: bool
