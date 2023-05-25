import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, ".env"))
except FileNotFoundError:
    pass

os.environ['DEVICE_FILENAME'] = os.getenv('DEVICE_FILENAME') or 'devices.csv'
