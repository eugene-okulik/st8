"""
Нужно прочитать файлик, который лежит в репозитории в моей папке. Здесь: homework/eugene_okulik/hw_15/data.txt
Файлик не копируйте и никуда не переносите.
Напишите программу, которая читает этот файл распечатывает из содержимого файла только большие буквы.
"""

import os
from pathlib import Path

file_dir = Path(os.path.dirname(__file__))
repository_root = file_dir.parent.parent.parent
lesson_path = os.path.join(repository_root, 'homework', 'eugene_okulik', "hw_15")
print(lesson_path)
lesson_file = os.path.join(lesson_path, 'data.txt')

with open(lesson_file, encoding='utf-8') as opened_file:
    file_data = opened_file.read()
    uppercase_letters = ''.join([char for char in file_data if char.isupper()])
    print(uppercase_letters)
