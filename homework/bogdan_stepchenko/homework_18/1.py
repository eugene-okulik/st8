from mysql import connector as mysql

with mysql.connect(
    username='st8',
    password='AVNS_7uWi-BfjZbsBVcxYXz5',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st8'
) as db:
    cursor = db.cursor(dictionary=True)

    def add_new_user(name: str, surname: str):
        query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
        cursor.execute(query, (name, surname))
        student_id = cursor.lastrowid
        db.commit()
        print(f'User with name: "{name}" and surname: "{surname}" was created.'
              f'\nHis/her id: {student_id}')
        return student_id

    def add_books_and_assign_to_user(titles: list, user_id: int):
        query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
        book_ids = []
        for title in titles:
            cursor.execute(query, (title, user_id))
            book_id = cursor.lastrowid
            book_ids.append(book_id)
            print(f'Book with title: "{title}" was created and assigned to user with id: {user_id}. '
                  f'\nBook id: {book_id}')
        db.commit()
        return book_ids

    def create_group(title: str, start_date: str, end_date: str):
        query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
        cursor.execute(query, (title, start_date, end_date))
        group_id = cursor.lastrowid
        db.commit()
        print(f'Group with name {title} was created. \nIts ID is: {group_id}')
        return group_id

    def assign_user_to_group(user_id: int, group_id: int):
        query = "UPDATE students SET group_id = %s WHERE id = %s"
        cursor.execute(query, (group_id, user_id))
        db.commit()
        print(f'User with id: {user_id} was assigned to group with id: {group_id}')

    def create_subject(title: str):
        query = "INSERT INTO subjects (title) VALUES (%s)"
        cursor.execute(query, (title,))
        subject_id = cursor.lastrowid
        print(f'Subject with title: {title} and id: {subject_id} was created')
        db.commit()
        return subject_id

    def create_lesson(title: str, subject_id: int):
        query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
        cursor.execute(query, (title, subject_id))
        lesson_id = cursor.lastrowid
        db.commit()
        print(f'Lesson with title: {title} was created and assigned to subject with id: {subject_id}')
        return lesson_id

    def set_mark_to_student(mark: int, lesson_id: int, student_id: int):
        query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (mark, lesson_id, student_id))
        db.commit()
        print(f'Mark: {mark} for lesson with id: {lesson_id}, was set to student with id: {student_id}')

    def get_all_student_marks(user_id: int):
        query = """
        SELECT s.name, s.second_name, l.title AS lesson_title, m.value AS mark_value, sub.title AS subject_title
        FROM students s
        JOIN marks m ON s.id = m.student_id
        JOIN lessons l ON m.lesson_id = l.id
        JOIN subjects sub ON l.subject_id = sub.id
        WHERE s.id = %s
        """
        cursor.execute(query, (user_id,))
        result = cursor.fetchall()
        for row in result:
            print(row)

    def get_all_book_for_student(student_id: int):
        query = """
        SELECT s.name, s.second_name, b.title
        FROM students s
        JOIN books b ON s.id = b.taken_by_student_id
        WHERE s.id = %s
        """
        cursor.execute(query, (student_id,))
        result = cursor.fetchall()
        for row in result:
            print(row)

    def get_whole_info_about_student(student_id: int):
        query = """
        SELECT s.name, s.second_name, g.title AS group_title, g.start_date, g.end_date, b.title AS book_title,
               su.title AS subject_title, l.title AS lesson_title, m.value AS mark_value
        FROM students s
        LEFT JOIN books b ON b.taken_by_student_id = s.id
        LEFT JOIN `groups` g ON g.id = s.group_id
        LEFT JOIN marks m ON m.student_id = s.id
        LEFT JOIN lessons l ON l.id = m.lesson_id
        LEFT JOIN `subjects` su ON su.id = l.subject_id
        WHERE s.id = %s
        """
        cursor.execute(query, (student_id,))
        result = cursor.fetchall()
        for row in result:
            print(row)

    # user creation:
    new_user_id = add_new_user('Catrine', 'McCalister')

    # books creation:
    new_book_ids = add_books_and_assign_to_user(['How to learn Spanish', 'Spanish. Grammar'], new_user_id)

    # group creation and assignment to student:
    new_group_id = create_group('Spanish A1', 'September 26', 'November 27')
    assign_user_to_group(new_user_id, new_group_id)

    # subject creation:
    new_subject_id = create_subject('Grammar')

    # lesson creation:
    new_lesson_id = create_lesson('Part One', new_subject_id)

    # setting mark to student
    set_mark_to_student(10, new_lesson_id, new_user_id)

    # getting all student marks
    get_all_student_marks(new_user_id)

    # getting all user' books
    get_all_book_for_student(new_user_id)

    # getting whole info about student
    get_whole_info_about_student(new_user_id)
