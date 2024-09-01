"""
Нужно прочитать файлик, который лежит в репозитории в моей папке. Здесь: homework/eugeny_okulik/hw_16/data.txt

Файлик не копируйте и никуда не переносите. Напишите программу, которая читает этот файл,
 находит в нём даты и делает с этими датами то, что после них написано. Опирайтесь на то,
 что структура каждой строки одинакова: сначала идет номер, потом дата, потом дефис и после него текст.
 У вас должен получиться код,
 который находит даты и для даты под номером один в коде должно быть реализовано то действие,
которое написано в файле после этой даты. Ну и так далее для каждой даты. Текст задания,
 который написан после даты распознавать не нужно, просто напишите код, который выполняет указанное действие.
"""

from datetime import datetime, timedelta
import os
from pathlib import Path

file_dir = Path(os.path.dirname(__file__))
repository_root = file_dir.parent.parent.parent
lesson_path = os.path.join(repository_root, 'homework', 'eugene_okulik', "hw_16")
print(lesson_path)
lesson_file = os.path.join(lesson_path, 'data.txt')

with open(lesson_file, encoding='utf-8') as opened_file:
    lines = opened_file.readlines()

for line in lines:
    parts = line.split(' - ')
    num_and_date = parts[0]
    date_str = num_and_date.split('. ')[1].strip()
    date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
    task = parts[1]

    if "неделю позже" in task:
        new_date = date + timedelta(weeks=1)
        print(f"Дата {date_str} на неделю позже: {new_date}")
    elif "день недели" in task:
        day_of_week = date.strftime("%A")
        print(f"Дата {date_str} приходится на день недели: {day_of_week}")
    elif "сколько дней назад" in task:
        current_date = datetime.now()
        days_ago = (current_date - date).days
        print(f"Дата {date_str} была {days_ago} дней назад")
