from mysql import connector
with connector.connect(
    user='st8',
    password='AVNS_7uWi-BfjZbsBVcxYXz5',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st8'
) as db:
    cursor = db.cursor(dictionary=True)
# добавляем студента
    cursor.execute(
        "INSERT INTO students (name, second_name) values ('Vasya','Vasechkin')")
    db.commit()
# добавляем 3 книги
    books = ['English level A', 'English level B', 'English level C']
    query = "INSERT INTO books (title, taken_by_student_id) values (%s, 155)"
    for book in books:
        cursor.execute(query, (book,))
        db.commit()
# добавляем группу
    cursor.execute(
        "INSERT INTO `groups` (title, start_date, end_date) values ('Bussines English','24-jan','24-aug')")
    db.commit()
# обновляем группу студента
    cursor.execute("UPDATE students SET group_id = 10 WHERE id = 154")
    db.commit()
# добавляем по 2 урока к 3 предметам
    subjects = ['Speaking', 'Watching', 'Listening']
    query2 = "INSERT INTO subjects (title) values (%s)"
    for subject in subjects:
        cursor.execute(query2, (subject,))
        db.commit()
    for i in [1, 2, 3]:
        for lesson in ['L1', 'L2']:
            cursor.execute(
                "INSERT INTO lessons (title, subject_id) values (%s, %s)", (lesson, i))
            db.commit()
# добавляем оценки
    lessonsids = [1, 2, 3, 4, 5, 6]
    query3 = "INSERT INTO marks (value, lesson_id, student_id) values (5, %s, 155)"
    for i in lessonsids:
        cursor.execute(query3, (i,))
        db.commit()
# получаем все оценки студента
    studId = 100
    cursor.execute(f'''
    SELECT s.name as 'Name', l.title as 'Lesson', m.value as 'Mark' FROM marks m
    LEFT JOIN lessons l on m.lesson_id = l.id
    LEFT JOIN students s on m.student_id = s.id
    WHERE student_id = {studId}''')
    print(cursor.fetchall())
# книги полученыые студентом
    cursor.execute(
        f"SELECT title from books b WHERE taken_by_student_id = {studId}")
    print(cursor.fetchall())
# вся информация о студенте
    cursor.execute(f'''

SELECT s.name as 'Name',
s.second_name as "Family",
g.title as 'Group',
b.title as 'Name of book',
m.value as 'Mark',
l.title as 'Lesson',
s2.title as 'Subject'
FROM students s
LEFT JOIN `groups` g on s.group_id = g.id
LEFT JOIN books b on s.id = b.taken_by_student_id
LEFT JOIN marks m on s.id = m.student_id
LEFT JOIN lessons l on l.id = m.lesson_id
LEFT JOIN subjects s2 on s2.id = l.subject_id
WHERE s.id = {studId}''')
    print(cursor.fetchall())
