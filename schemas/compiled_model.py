import datetime

from pydantic import BaseModel, Field
from pydantic.types import Optional

class CompiledModelBase(BaseModel):
    """"A Model that has been compiled with TFLite to fit a MCU.
    """
    created: datetime.datetime | None
    model_id: int  # relationship
    model_path: str


class CompiledModel(CompiledModelBase):
    """If CompiledModel is in database, it always has an id.
    """
    id: int

    class Config:
        orm_mode = True


class CompiledModelFile(CompiledModel):
    """With the compiled model file as string
    """

    file: str


class CompiledModelCreate(CompiledModelBase):
    """When creating a new CompiledModel, there is yet no id.
    """

    class Config:
        orm_mode = True
