insert into students (name, second_name, group_id) values ('Mikhail', 'Sorokin', 3)
insert into books (title, taken_by_student_id) values ('Martin Eden', 12)
insert into books (title, taken_by_student_id) values ('The White Fang', 12)
insert into books (title, taken_by_student_id) values ('A Wild Sheep Chase', 12)
insert into st8.groups (title, start_date, end_date) values ('How to be a good monkey', 'now', 'some day')
update st8.students set group_id=5 where id='12'
insert into subjeсts (title) values ('monkey language')
insert into subjeсts (title) values ('history')
insert into subjeсts (title) values ('bananalogy')
insert into lessons (title, subject_id) values ('bananas selection history', 8)
insert into lessons (title, subject_id) values ('how to get banana from humans', 8)
insert into lessons (title, subject_id) values ('banana stealing strategy', 8)
insert into lessons (title, subject_id) values ('Base grammar of mankey language', 7)
insert into lessons (title, subject_id) values ('dialects of mankey language', 7)
insert into lessons (title, subject_id) values ('History of ancient Rome', 6)
insert into lessons (title, subject_id) values ('Napoleonic wars', 6)
insert into marks (value, lesson_id, student_id) values ('5', 9, 12), ('5+', 10, 12), ('5+', 11, 12)
insert into marks (value, lesson_id, student_id) values ('5', 12, 12), ('5', 13, 12), ('5', 14, 12), ('5', 14, 12), ('4', 15, 12)
select value from marks where student_id=12 -- я тут хз только оценки или все забрать, но в любом случае
select * from books where taken_by_student_id =12 -- аналогично, нужно уточнять

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
WHERE students.id = 12;

 -- этот запрос не выполнил в итоге, дб ивер не видит таблицу subjects и все, я уже устал в эти танцы с бубнами играть
 -- все перепробовал
 -- постоянно что-то не так, даже точно за топой повторял и оно один хрен ошибки выводит порой. Это должно работать
 -- вот поэтому лучше новичкам в sql  pg admin показывать, Он хотя-бы работает нормально и без танцев с бубнами(сгорел)
