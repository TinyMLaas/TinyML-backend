from pydantic import BaseModel, Field

# Device always has these fields
class DeviceBase(BaseModel):
    name: str = Field(min_length=1)
    connection: str | None = Field(default=None, min_length=1)
    installer: str | None = Field(default=None, min_length=1)
    compiler: str | None = Field(default=None, min_length=1)
    model: str = Field(min_length=1)
    description: str = Field(min_length=1)

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
    
    
