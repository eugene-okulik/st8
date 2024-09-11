"""
Чет я упоролся в итоге делая это задание и намудрил. В свое оправдание скажу что на работе я все делаю нормально,
 запросы в отдельном файле в виде функций, ничего не зависит друг от друга и все такое.

Но когда я начинал писать эту колбасу мне казалось что идея замечательная, ну и в целом как будто не так уж плохо вышло
 ну по крайней мере главную цель оно выполняет
 Прими пожалуйста, я очень не хочу переделывать и правда умею использовать sql в питоне, честно;)

"""

from mysql import connector
from faker import Faker


class FakeData:
    fake = Faker()
    RANDOM_FIRST_NAME = fake.first_name()
    RANDOM_LAST_NAME = fake.last_name()
    RANDOM_BOOK_TITLE = fake.sentence(nb_words=3)
    RANDOM_JOB = fake.job()
    RANDOM_WORD = fake.word
    RANDOM_INT = fake.random_int
    FUTURE_DATE = fake.future_date()
    FAKE_DATE = fake.date()


class SqlQueries:
    student_ids = []
    group_ids = []
    subject_ids = []
    lessons_ids = []
    tables = {
        "books": "books",
        "st8.`groups`": "st8.`groups`",
        "lessons": "lessons",
        "marks": "marks",
        "students": "students",
        "subjects": "subjects"
    }

    @staticmethod
    def connect_to_db():
        return connector.connect(
            username='st8',
            password='AVNS_7uWi-BfjZbsBVcxYXz5',
            host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
            port=25060,
            database='st8'
        )

    @staticmethod
    def select_query(query, params=None):
        with SqlQueries.connect_to_db() as db:
            cursor = db.cursor(dictionary=True)
            cursor.execute(query, params or ())
            return cursor.fetchall()

    @staticmethod
    def insert_query(table_name, columns, values):
        tables = SqlQueries.tables

        if table_name not in tables:
            raise ValueError(f"Table {table_name} not found")

        columns_str = ', '.join(columns)
        placeholders = ', '.join(['%s'] * len(values))

        query = f"INSERT INTO {tables[table_name]} ({columns_str}) VALUES ({placeholders})"

        with SqlQueries.connect_to_db() as db:
            cursor = db.cursor(dictionary=True)
            cursor.execute(query, values)
            db.commit()

            if table_name == 'students':
                student_data = SqlQueries.select_query(
                    "SELECT id FROM students WHERE name=%s AND second_name=%s", (values[0], values[1])
                )
                if student_data:
                    SqlQueries.student_ids.append(student_data[0]['id'])
                else:
                    raise ValueError("Student not found after insertion")

            elif "groups" in table_name:
                group_data = SqlQueries.select_query("SELECT id FROM st8.`groups` WHERE title=%s", (values[0],))
                if group_data:
                    SqlQueries.group_ids.append(group_data[0]['id'])
                else:
                    raise ValueError("Group not found after insertion")

            elif table_name == "subjects":
                subject_data = SqlQueries.select_query("SELECT id FROM subjects WHERE title=%s", (values[0],))
                if subject_data:
                    SqlQueries.subject_ids.append(subject_data[0]['id'])
                else:
                    raise ValueError("Subject not found after insertion")

            elif table_name == "lessons":
                lesson_data = SqlQueries.select_query("SELECT id FROM lessons WHERE title=%s", (values[0],))
                if lesson_data:
                    SqlQueries.lessons_ids.append(lesson_data[0]['id'])
                else:
                    raise ValueError("Lesson not found after insertion")

    @staticmethod
    def insert_multi_query(table_name, columns, values):
        tables = SqlQueries.tables

        if table_name not in tables:
            raise ValueError(f"Table {table_name} not found")

        columns_str = ', '.join(columns)
        placeholders = ', '.join(['%s'] * len(columns))

        query = f"INSERT INTO {tables[table_name]} ({columns_str}) VALUES ({placeholders})"

        inserted_ids = []
        with SqlQueries.connect_to_db() as db:
            cursor = db.cursor(dictionary=True)

            for value_set in values:
                cursor.execute(query, value_set)
                inserted_ids.append(cursor.lastrowid)

            db.commit()

    @staticmethod
    def update_student_group(group_id, student_id):
        with SqlQueries.connect_to_db() as db:
            cursor = db.cursor()
            query = "UPDATE students SET group_id=%s WHERE id=%s"
            cursor.execute(query, (group_id, student_id))
            db.commit()


# Добавляю студента
SqlQueries.insert_query(
    table_name="students",
    columns=('name', 'second_name', 'group_id'),
    values=(FakeData.RANDOM_FIRST_NAME, FakeData.RANDOM_LAST_NAME, None)
)

# Создаю книгу и присваиваю ее предыдущему студенту
SqlQueries.insert_query(
    table_name="books",
    columns=('title', 'taken_by_student_id'),
    values=(FakeData.RANDOM_BOOK_TITLE, SqlQueries.student_ids[0])
)

# Создаю группу
SqlQueries.insert_query(
    table_name="st8.`groups`",
    columns=('title', 'start_date', 'end_date'),
    values=(f"{FakeData.RANDOM_JOB}",
            FakeData.FAKE_DATE, FakeData.FUTURE_DATE)
)

# Обновляю группу студента
SqlQueries.update_student_group(
    group_id=SqlQueries.group_ids[-1],
    student_id=SqlQueries.student_ids[-1]
)

# добавляю предмет
SqlQueries.insert_query(
    table_name="subjects",
    columns=('title',),
    values=(f"{FakeData.RANDOM_JOB}",)
)

# добавляю уроки
SqlQueries.insert_query(
    table_name="lessons",
    columns=('title', 'subject_id'),
    values=(f"{FakeData.RANDOM_WORD()}", f"{SqlQueries.subject_ids[0]}")
)

SqlQueries.insert_query(
    table_name="lessons",
    columns=('title', 'subject_id'),
    values=(f"{FakeData.RANDOM_WORD()}", f"{SqlQueries.subject_ids[0]}")
)

marks_values = [
    (FakeData.RANDOM_INT(1, 10), SqlQueries.lessons_ids[0], SqlQueries.student_ids[0]),
    (FakeData.RANDOM_INT(1, 10), SqlQueries.lessons_ids[1], SqlQueries.student_ids[0]),
]

# оценочки для уроков
SqlQueries.insert_multi_query(
    table_name="marks",
    columns=('value', 'lesson_id', 'student_id'),
    values=marks_values
)

# получение оценок
marks = SqlQueries.select_query("SELECT value FROM marks WHERE student_id = %s", (SqlQueries.student_ids[0],))
print(marks)

# получение книг
books = SqlQueries.select_query("SELECT * FROM books WHERE taken_by_student_id = %s", (SqlQueries.student_ids[0],))
print(books)

# общий селект
student_data = SqlQueries.select_query("""
SELECT
    students.id AS student_id,
    students.name,
    students.second_name,
    `groups`.title AS group_title,
    books.title AS book_title,
    lessons.title AS lesson_title,
    subjects.title AS subject_title,
    marks.value AS mark_value
FROM students
JOIN books ON students.id = books.taken_by_student_id
JOIN `groups` ON students.group_id = `groups`.id
JOIN marks ON students.id = marks.student_id
JOIN lessons ON marks.lesson_id = lessons.id
JOIN subjects ON lessons.subject_id = subjects.id
WHERE students.id = %s
""", (SqlQueries.student_ids[0],))
print(student_data)
