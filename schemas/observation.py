from pydantic import BaseModel, Field
from pydantic.types import Optional


class Observation(BaseModel):
    """Class for getting and returning values for observation
    """
    bridge_id: int
    device_id: int
    observation_value: dict