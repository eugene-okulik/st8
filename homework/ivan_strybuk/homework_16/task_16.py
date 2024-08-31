import os
import datetime
from pathlib import Path

file_dir = Path(os.path.dirname(__file__))
repository_root = file_dir.parent.parent.parent
eugene_okulik = os.path.join(repository_root, 'homework', 'eugene_okulik', 'hw_16')
eugene_file = os.path.join(eugene_okulik, 'data.txt')


def parsing_text(file_for_filtering) -> list:
    """обрабатываем файл по параметрам"""
    list_file = []
    for lines in file_for_filtering.splitlines():
        lines_formatting_right = lines.rsplit(' -', maxsplit=1)
        lines_formatting_left = lines_formatting_right[0].rsplit('. ', maxsplit=1)
        list_file.append(lines_formatting_left[1])
    return list_file


def parsing_text_for_datetime(str_for_datetime: str) -> datetime:
    """Приводим страку с датой в datetime"""
    python_date = datetime.datetime.strptime(str_for_datetime, '%Y-%m-%d %H:%M:%S.%f')
    return python_date


try:
    with open(eugene_file, 'r', encoding='utf-8') as opened_file:
        """
        task_1 распечатать эту дату, но на неделю позже. Должно получиться 2023-12-04 20:34:13.212967
        task_2 распечатать какой это будет день недели
        task_3 распечатать сколько дней назад была эта дата
        """

        file_read = opened_file.read()
        list_lines = parsing_text(file_read)
        task_1 = parsing_text_for_datetime(list_lines[0])
        task_2 = parsing_text_for_datetime(list_lines[1])
        task_3 = (datetime.datetime.now() - parsing_text_for_datetime(list_lines[2])).days
        print(f'{task_1}, через 7 дней будет {task_1 + datetime.timedelta(days=7)}')  # 2023-12-04 20:34:13.212967
        print(f'{task_2}, этот день был {task_1.strftime("%A")}')
        print(f'{parsing_text_for_datetime(list_lines[2])}, эта дата была {task_3} дня назад')

except FileNotFoundError:
    print(f'File {eugene_file} is missing!')
