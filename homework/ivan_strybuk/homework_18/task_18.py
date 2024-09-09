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
Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
(всё одним запросом с использованием Join)
Все запросы, которые сделаете, сохраняйте в файлик с расширением .txt или .sql, и сдавайте как обычно.
"""
from random import randrange
import names
import mysql.connector
from mysql.connector import Error

username = 'st8'
password = 'AVNS_7uWi-BfjZbsBVcxYXz5'
host = 'db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com'
port = 25060
database = 'st8'
int_random = randrange(10)


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


def execute_query(connect, query):
    cursor = connect.cursor()
    try:
        cursor.execute(query)
        id_data = cursor.lastrowid
        connect.commit()
        print("Query executed successfully")
        return id_data
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


# Подключение к БД
connection = create_connection(username, password, host, port, database)

# 1. Создайте студента (student)
first_name = names.get_first_name()
last_name = names.get_last_name()

create_students = f"INSERT INTO students (name, second_name, group_id) VALUES ('{first_name}', '{last_name}', NULL)"
create_new_student = execute_query(connection, create_students)
id_new_student = int(create_new_student)

# 2. Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
create_book_1 = f"INSERT INTO books (title, taken_by_student_id) VALUES ('Сказки {first_name}', NULL)"
create_book_2 = f"INSERT INTO books (title, taken_by_student_id) VALUES ('Рассказы {last_name}', NULL)"

id_new_book_1 = int(execute_query(connection, create_book_1))
id_new_book_2 = int(execute_query(connection, create_book_2))

update_book_description_1 = f'UPDATE books SET taken_by_student_id = {id_new_student} WHERE id = {id_new_book_1}'
update_book_description_2 = f'UPDATE books SET taken_by_student_id = {id_new_student} WHERE id = {id_new_book_2}'

execute_query(connection, update_book_description_1)
execute_query(connection, update_book_description_2)

# 3.Создайте группу (group) и определите своего студента туда
create_new_group = f"""
    INSERT INTO `groups` (title , start_date , end_date) VALUES ('AQA_{int_random}', 'March 24', 'August 24' )"""

id_new_groups = int(execute_query(connection, create_new_group))

update_students_group = f'UPDATE students SET group_id = {id_new_groups} WHERE id = {id_new_student}'

execute_query(connection, update_students_group)

# 4. Создайте несколько учебных предметов (subjects)
create_new_subjects_1 = f"INSERT INTO subjects (title) VALUES ('Story Music {int_random}')"
create_new_subjects_2 = f"INSERT INTO subjects (title) VALUES ('Kitchen {int_random}')"

id_subjects_1 = int(execute_query(connection, create_new_subjects_1))
id_subjects_2 = int(execute_query(connection, create_new_subjects_2))

# 5. Создайте по два занятия для каждого предмета (lessons)
create_new_lessons_1 = f"INSERT INTO lessons (title, subject_id) VALUES ('Lesson {str(int_random)}', {id_subjects_1})"
create_new_lessons_2 = f"INSERT INTO lessons (title, subject_id) VALUES ('Dance {str(int_random)}', {id_subjects_2})"

id_new_lesson_1 = int(execute_query(connection, create_new_lessons_1))
id_new_lesson_2 = int(execute_query(connection, create_new_lessons_2))

# 6. Поставьте своему студенту оценки (marks) для всех созданных вами занятий
subject_grades_1 = f"""
    INSERT INTO marks (value, lesson_id, student_id) VALUES ({int_random}, {id_new_lesson_1}, {id_new_student})"""
subject_grades_2 = f"""
    INSERT INTO marks (value, lesson_id, student_id) VALUES ({int_random}, {id_new_lesson_2}, {id_new_student})"""

execute_query(connection, subject_grades_1)
execute_query(connection, subject_grades_2)

# Получите информацию из базы данных:
# 1. Все оценки студента
all_student_grades = f"""
SELECT
    st.id,
    st.name,
    st.second_name,
    l.title lessons,
    su.title academic_subjects,
    m.value estimation
FROM 
    marks m
    JOIN students st ON m.student_id = st.id
    JOIN lessons l ON m.id = l.id 
    JOIN subjects su ON l.subject_id = su.id
WHERE
    m.student_id = {id_new_student}
"""

users = execute_read_query(connection, all_student_grades)
print("\n ID    Name    second_name    lessons    academic_subjects    estimation")
for user in users:
    print(user)

# 2. Все книги, которые находятся у студента
student_all_book = f"""
SELECT
    s.id,
    s.name,
    s.second_name,
    b.title as title_books
FROM
    students s
    LEFT JOIN books b ON s.id = b.taken_by_student_id
WHERE
    s.id = {id_new_student}
"""

users = execute_read_query(connection, student_all_book)
print("\n ID    Name    second_name    title_books")
for user in users:
    print(user)

# 3. Для вашего студента выведите всё, что о нем есть в базе: группа, книги,
# оценки с названиями занятий и предметов (всё одним запросом с использованием Join)
all_info_student = f"""
SELECT
    st.id,
    st.name,
    st.second_name,
    b.title book_name,
    gr.title group_name,
    gr.start_date,
    gr.end_date,
    l.title lessons,
    su.title academic_subjects,
    m.value estimation
FROM
    marks m
    JOIN students st ON m.student_id = st.id
    JOIN lessons l ON m.id = l.id
    JOIN subjects su ON l.subject_id = su.id
    JOIN `groups` gr ON st.group_id = gr.id
    JOIN books b ON st.id = b.taken_by_student_id
WHERE
    m.student_id = {id_new_student}
"""

users = execute_read_query(connection, all_info_student)
print("\n ID  name  second_name  book_name  group_name  start_date  end_date  lessons  academic_subjects  estimation")
for user in users:
    print(user)
