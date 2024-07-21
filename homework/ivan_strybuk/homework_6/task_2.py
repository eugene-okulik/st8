# Используя данные нужно получить сообщение.
# StudeDnts Ivanov, Petrov, Sidorov study these subjects: math, biology, geography

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students_str = ', '.join(students)  # Приведение списка в строку с указанием разделителя для отбора
subjects_str = ', '.join(subjects)

print('Students', students_str, end=" ")
print('study these subjects:', subjects_str)
