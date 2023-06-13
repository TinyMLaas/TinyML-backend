import os

from sqlalchemy.orm import Session
from schemas import schemas
from db import models
from config import DATASET_DIR
import cv2


def get_directory_size(path):
    """Returns the size of a directory containing subdirectories in megabytes.
    """

    total_size = 0

    for entry in os.scandir(path):
        if entry.is_file():
            total_size += entry.stat().st_size
        else:
            total_size += get_directory_size(entry.path)

    return total_size


def get_datasets(database: Session):
    """Returns a list schemas.Dataset objects
    of all available datasets in database.
    """
    result = database.query(models.Dataset).all()

    response = []

    for item in result:
        size = f"{get_directory_size(item.path)/1048576:.1f} MB"
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


def add_dataset(dataset_name, dataset_desc,database: Session):
    dataset = schemas.DatasetCreate(
        name=dataset_name,
        path="nopath",
        description=dataset_desc)
    db_dataset = models.Dataset(**dataset.dict())
    database.add(db_dataset)
    database.commit()
    database.refresh(db_dataset)
    db_dataset.path = f"{DATASET_DIR}{db_dataset.id}/"
    os.makedirs(db_dataset.path, exist_ok=True)
    size = f"{get_directory_size(db_dataset.path)/1048576:.1f} MB "
    db_dataset.size = size
    database.commit()
    database.refresh(db_dataset)
    return db_dataset


def add_image_to_dataset(dataset_id,files, database: Session):
    """ Adds all the images to the datasets folder

    Args:
        dataset_id: dataset where you will add the files to
        files: the files to be added to the path
        database: The db session you need for the path

    """ 
    dataset = database.query(models.Dataset).filter(
    models.Dataset.id == dataset_id).first()
    path = dataset.path
    for image in files:
        savedir = os.path.join(path,image.filename)
        with open(savedir, "wb+") as file_object:
            file_object.write(image.file.read())
