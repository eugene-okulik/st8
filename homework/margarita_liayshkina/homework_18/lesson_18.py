from mysql import connector
# import mysql.connector as mysql


with connector.connect(
    username="st8",
    password="AVNS_7uWi-BfjZbsBVcxYXz5",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st8"
) as db:
    cursor = db.cursor(dictionary=True)
    # создание студента

    def insert_student(name, second_name):
        query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
        cursor.execute(query, (name, second_name))
        student_id = cursor.lastrowid
        db.commit()
        print(f"Created student with ID: {student_id}")
        return student_id

    # создание нескольких книг:
    def insert_books(books, student_id):
        query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
        books_ids = []
        for book in books:
            cursor.execute(query, (book[0], student_id))
            book_id = cursor.lastrowid
            books_ids.append(book_id)
        db.commit()
        print(f"Books added with IDs: {books_ids}")
        return books_ids

    # cоздание  группы:
    def insert_group(group_title, start_date, end_date):
        query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
        cursor.execute(query, (group_title, start_date, end_date))
        group_id = cursor.lastrowid
        db.commit()
        print(f"Created group with ID: {group_id}")
        return group_id

    # добавление студента в группу:
    def assign_student_to_group(student_id, group_id):
        query = "UPDATE students SET group_id = %s WHERE id = %s"
        cursor.execute(query, (group_id, student_id))
        db.commit()
        print(f"Assigned student ID {student_id} to group ID {group_id}")

    # создание  нескольких учебных предметов:
    def insert_subjects(subjects):
        query = "INSERT INTO subjects  (title) VALUES (%s)"
        subjects_ids = []
        for subject in subjects:
            cursor.execute(query, (subject[0],))
            subject_id = cursor.lastrowid
            subjects_ids.append(subject_id)
        db.commit()
        print(f"Subjects added with IDs: {subjects_ids}")
        return subjects_ids

    # создание занятий:
    def insert_lesson(subject_id, lesson_titles):
        query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
        lessons_ids = []
        for title in lesson_titles:
            cursor.execute(query, (title, subject_id))
            lesson_id = cursor.lastrowid
            lessons_ids.append(lesson_id)
        db.commit()
        print(f"Lessons added with IDs: {lessons_ids}")
        return lessons_ids

    # создание оценок:
    def insert_marks(value, lesson_id, student_id):
        query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (value, lesson_id, student_id))
        db.commit()
        print(f"Mark {value} added for student ID {student_id} for lesson ID {lesson_id}")

    ###################################################
    def get_all_marks(student_id):
        query = "SELECT value FROM marks m  WHERE student_id = %s"
        cursor.execute(query, (student_id,))
        data = cursor.fetchall()
        print(data)

    def get_all_books(student_id):
        query = "SELECT  title  FROM books b  WHERE taken_by_student_id =  %s"
        cursor.execute(query, (student_id,))
        data_book = cursor.fetchall()
        print(data_book)

    def all_info_about_current_student(student_id):
        big_query = ('''
        SELECT
        s.id AS student_id,
        s.name AS student_name,
        s.second_name AS student_second_name,
        g.title AS group_title,
        b.title AS book_title,
        m.value AS mark_value,
        l.title AS lesson_title,
        sub.title AS subject_title
        FROM students s JOIN `groups` g ON s.group_id = g.id
        LEFT JOIN books b ON b.taken_by_student_id = s.id
        LEFT JOIN marks m ON s.id = m.student_id
        LEFT JOIN lessons l ON m.lesson_id = l.id
        LEFT JOIN subjects sub ON l.subject_id = sub.id
        WHERE s.id = %s
        ''')
        cursor.execute(big_query, (student_id,))
        full_data = cursor.fetchall()
        print(f'All info about student with ID{student_id}: {full_data}')

    #######################################################
    # Вызовы всех функций  по INSERT  и присвоение значений:
    # 1
    student_id = insert_student('Margarita', 'Liaushkina')

    # 2
    books = [('Literatura_4',), ('Matematic_3',), ('Algebra3',)]
    insert_books(books, student_id)
    # 3
    group_id = insert_group('Techical Faculty_3', '2024-10-24', '2024-10-24')
    assign_student_to_group(student_id, group_id)

    # 4
    subjects = [('Subject_1',), ('Subgect_2',), ('Subject_0',)]
    inserted_subj = insert_subjects(subjects)

    # 5, 6
    lesson_titles = ['Lesson 1', 'Lesson 2']
    for subject_id in inserted_subj:
        lessons_ids = insert_lesson(subject_id, lesson_titles)
        for one_lesson_id in lessons_ids:
            insert_marks("4", one_lesson_id, student_id)

    #  вызовы функций по SELECT
    get_all_marks(student_id)
    get_all_books(student_id)
    all_info_about_current_student(student_id)
