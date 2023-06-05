from ipaddress import IPv4Address
from pydantic import BaseModel, Field


class DeviceBase(BaseModel):
    """Base for Device model. Lacks id as it is assigned by database.
    """
    name: str = Field(min_length=1)
    connection: str | None = Field(default=None, min_length=1)
    installer: str | None = Field(default=None, min_length=1)
    compiler: str | None = Field(default=None, min_length=1)
    model: str = Field(min_length=1)
    description: str = Field(min_length=1)
    serial:  str = Field(min_length=1)


class Device(DeviceBase):
    """If Device is in database, it always has an id.
    """
    id: int

    class Config:
        orm_mode = True


class DeviceCreate(DeviceBase):
    """When creating a new Device, there is yet no id.
    """

    class Config:
        orm_mode = True


class BridgeBase(BaseModel):
    """Base for Bridge model. Lacks id as it is assigned by database.
    """
    ip_address: IPv4Address
    name: str | None = None


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

class DatasetBase(BaseModel):
    """Base for Dataset model. Lacsk id as it is assigned by database
    """
    path: str = Field(min_length=1)
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    size: str = Field(min_length=1)

class Dataset(DatasetBase):
    """If Bridge is in database, it always has an id.
    """
    id: int

    class Config:
        orm_mode = True
