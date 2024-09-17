import csv
import os

from connection import connect_to_db


def books_from_file(file):
    root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    path = os.path.join(root, 'eugene_okulik', 'Lesson_19', 'for_hw')
    data = os.path.join(path, file)
    titles = []
    try:
        with open(data, encoding='utf-8') as csv_file:
            file = csv.DictReader(csv_file)
            title_and_name = list(file)
            for value in title_and_name:
                book = value['title']
                titles.append(book)
    except FileNotFoundError as error:
        print(error)
    return titles


def groups_for_students(connection, titles):
    groups = []
    for book in titles:
        cursor = connection.cursor()
        query = """SELECT b.title AS book_title, s.name AS student_name, g.title AS group_title
            FROM students s
            LEFT JOIN `groups` g ON g.id = s.group_id
            JOIN books b ON b.taken_by_student_id = s.id
            WHERE b.title = %s"""
        cursor.execute(query, (book,))
        result = cursor.fetchall()
        groups.append(result)

    print(groups)


groups_for_students(connect_to_db(), books_from_file('books.csv'))
