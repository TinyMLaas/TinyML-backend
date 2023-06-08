import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, ".env"))
except FileNotFoundError:
    pass

os.environ["DATABASE_URL"] = os.getenv("DATABASE_URL")
DATASET_DIR = os.getenv("DATASET_DIR")
MODEL_DIR = os.getenv("MODEL_DIR") or "tensorflow_models/"
