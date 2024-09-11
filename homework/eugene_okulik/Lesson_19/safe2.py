from mysql import connector
import os
import dotenv
dotenv.load_dotenv(override=True)


print(os.getenv('DB_PASSW'))
with connector.connect(
    username=os.getenv('ST8_USERNAME'),
    password=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
) as db:
    cursor = db.cursor(dictionary=True)

    cursor.execute('SELECT * FROM students')
    data = cursor.fetchall()
    print(data)
    for line in data:
        print(line['second_name'])
