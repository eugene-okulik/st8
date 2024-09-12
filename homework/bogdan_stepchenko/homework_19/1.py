import csv
import os
from pathlib import Path
from connection import connect_to_db


def getting_books_from_file(file_name: str):
    repository_root = Path(os.path.dirname(__file__)).parent.parent.parent
    target_file = os.path.join(repository_root, 'homework', 'eugene_okulik', 'Lesson_19', 'for_hw', file_name)
    book_names = []
    try:
        with open(target_file, 'r') as opened_csv_file:
            data = csv.DictReader(opened_csv_file)
            data = list(data)
            book_names = [name['title'] for name in data]
            print(book_names)
    except FileNotFoundError as error:
        print(error)
    return book_names


def get_user_group_according_to_book(connection, book_names: list):
    group_names = []
    for book_name in book_names:
        cursor = connection.cursor()
        query = """
        SELECT b.title AS book_title, s.name AS student_name, g.title AS group_title
        FROM students s
        LEFT JOIN `groups` g ON g.id = s.group_id
        JOIN books b ON b.taken_by_student_id = s.id
        WHERE b.title = %s;
        """
        cursor.execute(query, (book_name,))
        result = cursor.fetchall()
        for book_title, student_name, group_title in result:
            if group_title:
                print(
                    f"Пользователь, который взял книгу '{book_title}', "
                    f"имеет имя '{student_name}' и учится в группе '{group_title}'."
                )
                group_names.append(group_title)
            else:
                print(
                    f"Пользователь, который взял книгу '{book_title}', "
                    f"имеет имя '{student_name}', но не находится в группе.")
                group_names.append('-user without group-')
        cursor.close()
    print(group_names)
    return group_names


get_user_group_according_to_book(connect_to_db(), getting_books_from_file('books.csv'))
