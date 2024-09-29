import os
import csv
import dotenv
from pathlib import Path
from mysql import connector

dotenv.load_dotenv(override=True)

with connector.connect(
    username=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
) as db:
    cursor = db.cursor(dictionary=True)

    try:
        file_dir = Path(os.path.dirname(__file__))
        repository_root = file_dir.parent.parent

        eugene_path = os.path.join(repository_root, 'eugene_okulik', 'Lesson_19', 'for_hw')
        eugene_file = os.path.join(eugene_path, 'books.csv')

        with open(eugene_file, encoding='utf-8', newline='') as opened_file:
            read_file_data = csv.reader(opened_file)
            for line in read_file_data:

                book_query = '''
                SELECT DISTINCT(g.title) FROM students s
                LEFT JOIN `books` b ON b.taken_by_student_id = s.id
                LEFT JOIN `groups` g ON g.id  = s.group_id
                WHERE b.taken_by_student_id IS NOT NULL AND s.group_id IS NOT NULL AND b.title = %s
                '''

                cursor.execute(book_query, line)
                group_titles = cursor.fetchall()
                for one_group in group_titles:
                    print(f"Group title = {one_group['title']}")

    except FileNotFoundError as error:
        print(f"Error: {error}")
