import os
from mysql import connector as sql
import dotenv
dotenv.load_dotenv()


def connect_to_db():
    connection = None
    try:
        connection = sql.connect(
            username=os.getenv('DB_USERNAME'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            database=os.getenv('DB_NAME')
        )
    except sql.Error as error:
        print(f'Next error has been occurred: {error}')
    return connection
