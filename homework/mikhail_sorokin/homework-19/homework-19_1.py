"""
Прочитайте csv файл, который находится в моей папке homework/eugene_okulik/Lesson_19/for_hw.
 Файл не копируйте и никуда не переносите, путь постройте так, чтобы ваша программа работала на любом компе.

Из файла вы получите названия книг. Получите из базы данных названия групп, в которых учатся те студенты,
у которых сейчас на руках перечисленные книги. Полученные названия групп распечатайте.

При подключении к базе данных используйте подход .env, чтобы данные для подключения к базе не улетели в гитхаб.
"""
import os
from config import Config
from pathlib import Path
from mysql import connector


class SqlQueries:

    def __init__(self):
        self.host = Config.DB_HOST
        self.port = Config.DB_PORT
        self.user = Config.DB_USERNAME
        self.password = Config.DB_PASSWORD
        self.database = Config.DB_NAME

    def connect_to_db(self):
        return connector.connect(
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database
        )

    def select_query(self, query, params=None):
        with SqlQueries.connect_to_db(self) as db:
            cursor = db.cursor(dictionary=True)
            cursor.execute(query, params or ())
            return cursor.fetchall()


def read_file_and_get_names():
    file_dir = Path(os.path.dirname(__file__))
    repository_root = file_dir.parent.parent.parent
    lesson_path = os.path.join(repository_root, 'homework', 'eugene_okulik', "Lesson_19", "for_hw")
    lesson_file = os.path.join(lesson_path, 'books.csv')

    with open(lesson_file, encoding='utf-8') as opened_file:
        lines = opened_file.readlines()
        books = [line.strip() for line in lines]
    return books[1:]


def get_group_titles():
    sql_queries = SqlQueries()

    query_books = """
    SELECT taken_by_student_id FROM books
    WHERE title IN (%s, %s, %s, %s)
    """

    book_titles = read_file_and_get_names()
    student_ids_result = sql_queries.select_query(query_books, book_titles)
    student_ids = [row['taken_by_student_id'] for row in student_ids_result]
    print(f"Taken by student IDs: {student_ids}")

    student_ids_tuple = tuple(student_ids)

    placeholders = ','.join(['%s'] * len(student_ids_tuple))
    query_students = f"""
    SELECT group_id FROM students
    WHERE id IN ({placeholders})
    """

    print(f"Student IDs: {student_ids_tuple}")

    group_ids_result = sql_queries.select_query(query_students, student_ids_tuple)
    group_ids = [row['group_id'] for row in group_ids_result]
    print(f"Group IDs: {group_ids}")

    group_ids_tuple = tuple(group_ids)
    placeholders = ','.join(['%s'] * len(group_ids_tuple))

    query_groups = f"""
    SELECT title FROM `groups` 
    WHERE id IN ({placeholders})
    """
    group_titles_result = sql_queries.select_query(query_groups, group_ids_tuple)
    group_titles = [row['title'] for row in group_titles_result]
    print(f"Group Titles: {group_titles}")


get_group_titles()
