# Задание
## Создайте в базе данных полный набор информации о студенте, заполнив все таблички:

### 1. Создайте студента (student)

```
INSERT INTO students (name, second_name, group_id) VALUES ('Ivan', 'Strybuk', NULL)
```
- зачисление в группу

```
UPDATE students SET group_id = 3 WHERE id = 10
```

### 2. Создайте несколько книг (books) и укажите, что ваш созданный студент взял их

```
INSERT INTO books (title, taken_by_student_id) VALUES ('Naruto', 10)
```

### 3.Создайте группу (group) и определите своего студента туда

```
INSERT INTO `groups` (title , start_date , end_date) VALUES ('TT 34', 'March 24', 'August' )
```

- установка оканчяния

```
UPDATE `groups` SET end_date ='August 24' WHERE id = 3
```

### 4. Создайте несколько учебных предметов (subjects)

```
INSERT INTO subjeсts (title) VALUES ('Music')
INSERT INTO subjeсts (title) VALUES ('Python')
```

### 5. Создайте по два занятия для каждого предмета (lessons)

```
INSERT INTO lessons (title, subject_id) VALUES ('Studying the topic: 1', 5)
INSERT INTO lessons (title, subject_id) VALUES ('Dance party', 4)
```

### 6. Поставьте своему студенту оценки (marks) для всех созданных вами занятий

```
INSERT INTO marks (value, lesson_id, student_id) VALUES ('A+', 7, 10)
INSERT INTO marks (value, lesson_id, student_id) VALUES (7, 5, 10)
```

# Получите информацию из базы данных:

### 1. Все оценки студента

```
SELECT st.name, st.second_name, l.title lessons, su.title academic_subjects, m.value estimation 
FROM marks m 
JOIN students st ON m.student_id = st.id
JOIN lessons l ON m.id = l.id 
JOIN subjeсts su ON l.subject_id = su.id
WHERE m.student_id = 10
```

### 2. Все книги, которые находятся у студента

```
SELECT s.name, s.second_name, b.title as title_books FROM students s 
LEFT JOIN books b ON s.id = b.taken_by_student_id 
WHERE s.id = 10
```

### 3. Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов (всё одним запросом с использованием Join)

```
SELECT st.name, st.second_name, b.title book_name, gr.title group_name, gr.start_date, gr.end_date, l.title lessons, su.title academic_subjects, m.value estimation 
FROM marks m 
JOIN students st ON m.student_id = st.id
JOIN lessons l ON m.id = l.id 
JOIN subjeсts su ON l.subject_id = su.id
JOIN `groups` gr ON st.group_id = gr.id 
JOIN books b ON st.id = b.taken_by_student_id 
WHERE m.student_id = 10
```