from dotenv import load_dotenv
import os


class Config:
    load_dotenv()

    DB_USERNAME = os.getenv('ST8_DB_USERNAME')
    DB_PASSWORD = os.getenv('ST8_DB_PASSWORD')
    DB_NAME = os.getenv('ST8_DB_NAME')
    DB_HOST = os.getenv('ST8_DB_HOST')
    DB_PORT = os.getenv('ST8_DB_PORT')
