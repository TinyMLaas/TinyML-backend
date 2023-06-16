from pydantic import BaseModel, Field
from pydantic.types import Optional


class DatasetBase(BaseModel):
    """Base for Dataset model. Lacks id as it is assigned by database
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


class DatasetCreate(BaseModel):
    """When creating a new Dataset, there is yet no id. There is also no size to save.
    """
    path: str = Field(min_length=1)
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
