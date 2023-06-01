from pydantic import BaseModel, Field
from ipaddress import IPv4Address


# Device always has these fields
class DeviceBase(BaseModel):
    name: str = Field(min_length=1)
    connection: str | None = Field(default=None, min_length=1)
    installer: str | None = Field(default=None, min_length=1)
    compiler: str | None = Field(default=None, min_length=1)
    model: str = Field(min_length=1)
    description: str = Field(min_length=1)
    serial:  str = Field(min_length=1)

# when you read a device, it has gained an id
class Device(DeviceBase):
    id: int
    
    # without this, everything explodes!!
    class Config:
        orm_mode = True

# when creating, there is no id so use the basemodel
class DeviceCreate(DeviceBase):
    pass

    class Config:
        orm_mode = True    
    

class BridgeBase(BaseModel):
    ip_address: IPv4Address
    name: str | None = None
    
    
class Bridge(BridgeBase):
    id: int
    
    class Config:
        orm_mode = True
    
    
class BridgeCreate(BridgeBase):
    pass

    class Config:
        orm_mode = True
    
