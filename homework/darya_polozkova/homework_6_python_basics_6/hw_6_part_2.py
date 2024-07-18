students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

# Распечатайте текст, который будет использовать данные из этих списков.
# Текст в итоге должен выглядеть так:
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography
students_str = ', '.join(students)
subjects_str = ', '.join(subjects)
print(f'Students {students_str} study these subjects: {subjects_str}')
