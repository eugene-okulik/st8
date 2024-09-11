from mysql import connector as sql


with sql.connect(
    username='st8',
    password='AVNS_7uWi-BfjZbsBVcxYXz5',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st8'
) as db:
    cursor = db.cursor(dictionary=True)

    def create_student(name, second_name):
        cursor.execute("INSERT INTO students (name, second_name) VALUES (%s, %s)", (name, second_name))
        st_id = cursor.lastrowid
        db.commit()
        print(f'Student {name} {second_name} is created')
        return st_id

    def assign_books(titles, taken_by_student_id):
        query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
        books_ids = []
        for title in titles:
            cursor.execute(query, (title, taken_by_student_id))
            books_ids.append(cursor.lastrowid)
        db.commit()
        return books_ids

    def create_a_group(title, start_date, end_date):
        cursor.execute("INSERT INTO `groups` (title, start_date, end_date)"
                       " VALUES (%s, %s, %s)", (title, start_date, end_date))
        gr_id = cursor.lastrowid
        db.commit()
        print(f'Your group is {title}')
        return gr_id

    def assign_group_to_a_student(st_id, gr_id):
        query = "UPDATE students SET group_id = %s WHERE id = %s"
        cursor.execute(query, (gr_id, st_id))
        db.commit()

    def create_subject():
        query = "INSERT INTO subjects (title) VALUES (%s)"
        subjects = ['Yammy', 'Bunny']
        subjects_ids = []
        for subject in subjects:
            cursor.execute(query, (subject,))
            subjects_ids.append(cursor.lastrowid)
        db.commit()
        return subjects_ids

    def create_lessons(subjects_ids):
        query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
        lessons = [('Make-up', subjects_ids[0]),
                   ('Lashes', subjects_ids[0]),
                   ('Hair', subjects_ids[1]),
                   ('Dress', subjects_ids[1])]
        lessons_id = []
        for lesson in lessons:
            cursor.execute(query, lesson)
            lessons_id.append(cursor.lastrowid)
            db.commit()
        return lessons_id

    def assign_marks(mark, lesson_id, st_id):
        query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (mark, lesson_id, st_id))
        db.commit()

    def get_all_student_marks(st_id):
        query = "SELECT value FROM marks WHERE student_id = %s"
        cursor.execute(query, (st_id,))
        result = cursor.fetchall()
        print(result)

    def get_all_book_for_student(st_id):
        query = "SELECT title FROM books WHERE taken_by_student_id = %s;"
        cursor.execute(query, (st_id,))
        books = cursor.fetchall()
        print(f'Student has taken ', books)


    def get_whole_info_about_student(st_id):
        query = ("""SELECT s.id, s.name, s.second_name, b.title book_name, gr.title group_name, gr.start_date, gr.end_date,
                 l.title lessons, su.title academic_subjects, m.value estimation 
                 FROM marks m
                 JOIN students s ON m.student_id = s.id
                 JOIN lessons l ON m.id = l.id
                 JOIN subjects su ON l.subject_id = su.id
                 JOIN `groups` gr ON s.group_id = gr.id
                 JOIN books b ON s.id = b.taken_by_student_id
                 WHERE m.student_id = %s""")
        cursor.execute(query, (st_id,))
        result = cursor.fetchall()
        print(f'Your students info: {result}')


    st_id = create_student('Monica', 'Beluchi')
    book_id = assign_books(['Beauty', 'Fashion', 'Love'], st_id)
    gr_id = create_a_group('star', '2 Sep 2010', '2 May 2030')
    assign_group_to_a_student(st_id, gr_id)
    subjects_id = create_subject()
    lessons_id = create_lessons(subjects_id)
    assign_marks('10', lessons_id[0], st_id)
    assign_marks('11', lessons_id[1], st_id)
    assign_marks('12', lessons_id[2], st_id)
    assign_marks('13', lessons_id[3], st_id)
    get_all_student_marks(st_id)
    get_all_book_for_student(st_id)
    get_whole_info_about_student(st_id)
