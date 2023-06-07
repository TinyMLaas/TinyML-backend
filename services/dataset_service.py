import os

from sqlalchemy.orm import Session
from schemas import schemas
from db import models


def get_directory_size(path):
    """Returns the size of a directory containing subdirectories in megabytes.
    """

    total_size = 0

    for entry in os.scandir(path):
        if entry.is_file():
            total_size += entry.stat().st_size
        else:
            total_size += get_directory_size(entry.path)

    return total_size / 1024


def get_datasets(database: Session):
    """Returns a list schemas.Dataset objects
    of all available datasets in database.
    """
    result = database.query(models.Dataset).all()

    response = []

    for item in result:
        size = f"{get_directory_size(item.path):.1f} MB"
        dataset = schemas.Dataset(
            id=item.id,
            name=item.name,
            path=item.path,
            description=item.description,
            size=size)
        response.append(dataset)

    return response


def get_dataset_path_by_id(database: Session, id: int):
    """Returns a dataset based on id. Used for getting wanted
    dataset for tensorflow training
    """

    result = database.query(models.Dataset).filter(models.Dataset.id == id).one()
    return result.path