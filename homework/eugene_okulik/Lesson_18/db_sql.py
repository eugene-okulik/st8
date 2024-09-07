from mysql import connector
# import mysql.connector as mysql


with connector.connect(
    username='st8',
    password='AVNS_7uWi-BfjZbsBVcxYXz5',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st8'
) as db:
    cursor = db.cursor(dictionary=True)

    def select():
        cursor.execute('SELECT * FROM students')
        data = cursor.fetchall()
        print(data)
        for line in data:
            print(line['second_name'])

    def get_one():
        cursor.execute('SELECT * FROM students WHERE id = 1')
        data = cursor.fetchone()
        print(data)
        print(data['second_name'])

    def db_insert():
        cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('From', 'Python', 1)")
        student_id = cursor.lastrowid
        db.commit()
        print(student_id)

    def incorrect_format():
        name = "From'; -- "
        second_name = '!!!!!Python!!!!!'
        cursor.execute(f"SELECT * FROM students WHERE name = '{name}' AND second_name = '{second_name}'")
        data = cursor.fetchall()
        if data:
            print('data exists')
        else:
            print('no data')
        # print(data)

    def correct_formatting():
        # name = "From'; -- "
        name = "From"
        # second_name = '!!!!!Python!!!!!'
        second_name = 'Python'
        query = f"SELECT * FROM students WHERE name = %s AND second_name = %s"
        cursor.execute(query, (name, second_name))
        data = cursor.fetchall()
        if data:
            print('data exists')
        else:
            print('no data')

    def one_param_formatting():
        second_name = 'Python'
        query = f"SELECT * FROM students WHERE second_name = %s"
        cursor.execute(query, (second_name,))
        data = cursor.fetchall()
        print(data)

    def multy_insert():
        # query = "insert into books (title) VALUES (%s)"
        # cursor.executemany(query, [('как я провел свое лето',), ('Harry Potter',), ('Sun',)])
        # book_id = cursor.lastrowid
        # db.commit()
        # print(book_id)

        books = [('как я провел свое лето',), ('Harry Potter',), ('Sun',)]
        query = "insert into books (title) VALUES (%s)"
        books_ids = []
        for book in books:
            cursor.execute(query, book)
            books_ids.append(cursor.lastrowid)
        db.commit()
        print(books_ids)

big_query = '''
SELECT s.name, b.title as book_title, g.title as group_title FROM students st
left JOIN books bks
ON s.id = b.taken_by_student_id
left JOIN `groups` gr
ON s.group_id = g.id
WHERE s.id = %s
'''
