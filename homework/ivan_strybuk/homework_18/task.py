"""
Задание
Создайте в базе данных полный набор информации о студенте, заполнив все таблички:

Создайте студента (student)
Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
Создайте группу (group) и определите своего студента туда
Создайте несколько учебных предметов (subjects)
Создайте по два занятия для каждого предмета (lessons)
Поставьте своему студенту оценки (marks) для всех созданных вами занятий

Получите информацию из базы данных:
Все оценки студента
Все книги, которые находятся у студента
Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов (всё одним запросом с использованием Join)
Все запросы, которые сделаете, сохраняйте в файлик с расширением .txt или .sql, и сдавайте как обычно.

"""
#
# from mysql import connector
#
# with connector.connect(
#         username='st8',
#         password='AVNS_7uWi-BfjZbsBVcxYXz5',
#         host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
#         port=25060,
#         database='st8'
# ) as db:
#     cursor = db.cursor(dictionary=True)
#
#
#     def select():
#         cursor.execute('SELECT * FROM students')
#         data = cursor.fetchall()
#         print(data)
#         for line in data:
#             print(line['second_name'])
#
#
#     def get_one():
#         cursor.execute('SELECT * FROM students')
#         data = cursor.fetchone()
#         print(data)
#         print(data['second_name'])
#
#
#     def db_insert():
#         cursor.execute('INSERT INTO')
#         student_id = cursor.lastrowid
#         db.commit()
#         print(student_id)

import mysql.connector
from mysql.connector import Error

username = 'st8'
password = 'AVNS_7uWi-BfjZbsBVcxYXz5'
host = 'db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com'
port = 25060
database = 'st8'


def create_connection(user_name, passwd, host_name, port_name, db):
    connection = None
    try:
        connection = mysql.connector.connect(
            username=user_name,
            password=passwd,
            host=host_name,
            port=port_name,
            database=db
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        id_data = cursor.lastrowid
        connection.commit()
        print("Query executed successfully")
        return id_data
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


# Подключение к БД
connection = create_connection(username, password, host, port, database)

# 1. Создайте студента (student)
create_students = "INSERT INTO students (name, second_name, group_id) VALUES ('Tom', 'Di', NULL)"
create_new_student = execute_query(connection, create_students)
id_new_student = int(create_new_student)
print(id_new_student)

# 2. Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
create_book_1 = "INSERT INTO books (title, taken_by_student_id) VALUES ('Сказки том 1', NULL)"
create_book_2 = "INSERT INTO books (title, taken_by_student_id) VALUES ('Сказки том 2', NULL)"

id_new_book_1 = int(execute_query(connection, create_book_1))
id_new_book_2 = int(execute_query(connection, create_book_2))

update_book_description_1 = f'UPDATE books SET taken_by_student_id = {id_new_student} WHERE id = {id_new_book_1}'
update_book_description_2 = f'UPDATE books SET taken_by_student_id = {id_new_student} WHERE id = {id_new_book_2}'

execute_query(connection, update_book_description_1)
execute_query(connection, update_book_description_2)

# 3.Создайте группу (group) и определите своего студента туда
create_new_group = "INSERT INTO `groups` (title , start_date , end_date) VALUES ('AQA_P', 'March 24', 'August 24' )"

id_new_groups = int(execute_query(connection, create_new_group))

update_students_group = f'UPDATE students SET group_id = {id_new_groups} WHERE id = {id_new_student}'

execute_query(connection, update_students_group)

# 4. Создайте несколько учебных предметов (subjects)
create_new_subjeсts_1 = "INSERT INTO subjects (title) VALUES ('Music_pop')"
create_new_subjeсts_2 = "INSERT INTO subjects (title) VALUES ('Music_dance')"

id_new_subjects_1 = int(execute_query(connection, create_new_subjeсts_1))
id_new_subjects_2 = int(execute_query(connection, create_new_subjeсts_2))

# 5. Создайте по два занятия для каждого предмета (lessons)
create_new_lessons_1 = f"INSERT INTO lessons (title, subject_id) VALUES ('Dance pop party', {id_new_subjects_1})"
create_new_lessons_2 = f"INSERT INTO lessons (title, subject_id) VALUES ('Dance party', {id_new_subjects_2})"

id_new_lesson_1 = int(execute_query(connection, create_new_lessons_1))
id_new_lesson_2 = int(execute_query(connection, create_new_lessons_2))

# 6. Поставьте своему студенту оценки (marks) для всех созданных вами занятий
subject_grades_1 = f"INSERT INTO marks (value, lesson_id, student_id) VALUES (9, {id_new_lesson_1}, {id_new_student})"
subject_grades_2 = f"INSERT INTO marks (value, lesson_id, student_id) VALUES (7, {id_new_lesson_2}, {id_new_student})"

execute_query(connection, subject_grades_1)
execute_query(connection, subject_grades_2)
