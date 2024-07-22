"""
Даны такие списки:

students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']

Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:

Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography
"""

students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']

students_str, subjects_str = ', '.join(students), ', '.join(subjects)

string = f"{students_str} study these subjects: {subjects_str}"

print(string)
