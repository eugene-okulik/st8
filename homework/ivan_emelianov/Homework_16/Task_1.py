import os
from pathlib import Path
from datetime import datetime, timedelta


def open_file(file: str):

    rep_root = Path(os.path.dirname(__file__)).parent.parent.parent

    file_path = os.path.join(rep_root, 'homework', 'eugene_okulik', 'hw_16', f'{file}')

    with open(file_path, 'r', encoding='utf-8') as opened_file:
        return opened_file.readlines()


def process_list(line):
    parts = line.split(' - ')

    first_part = parts[0].split(' ', maxsplit=1)
    number = int(first_part[0].replace('.', ''))
    date_str = first_part[1]

    date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

    if number == 1:
        new_date = date + timedelta(weeks=1)
        print(f'Дата на неделю позже: {new_date}')

    elif number == 2:
        day_of_week = date.strftime('%A')
        print(f'День недели: {day_of_week}')

    elif number == 3:
        time_now = datetime.now()
        days_ago = time_now - date
        print(f'Это было {days_ago.days} дней назад')


def process_instructions(file_path: str):
    lines = open_file(file_path)

    list(map(process_list, lines))


if __name__ == "__main__":
    file_name = "data.txt"
    process_instructions(file_name)
