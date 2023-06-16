from enum import Enum

from pydantic import BaseModel, Field
from pydantic.types import Optional


class LossFunctions(str, Enum):
    """Loss functions available in training
    """

    categorical_crossentropy = "Categorical crossentropy"
    sparse_categorical_crossentropy = "Sparse Categorical crossentropy"
