from mysql import connector
import secrets


with connector.connect(
    username=secrets.username,
    password=secrets.password,
    host=secrets.host,
    port=secrets.port,
    database=secrets.database
) as db:
    cursor = db.cursor(dictionary=True)

    cursor.execute('SELECT * FROM students')
    data = cursor.fetchall()
    print(data)
    for line in data:
        print(line['second_name'])
