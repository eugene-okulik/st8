import os
from pathlib import Path
from datetime import datetime, timedelta


def parse_of_date(line: str) -> datetime:
    date_str = ' '.join(line.split()[1:3])
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")


def getting_line_from_text(number: int, text: [str]):
    for line in filter(lambda x: x.startswith(f'{number}'), text):
        return line


def using_dates_from_file(file: str):

    repository_root = Path(os.path.dirname(__file__)).parent.parent.parent
    target_file = os.path.join(repository_root, 'homework', 'eugene_okulik', 'hw_16', file)
    try:
        with open(target_file, 'r', encoding='utf-8') as opened_file:
            data = opened_file.read()
            lines = data.splitlines()

            line_1 = getting_line_from_text(1, lines)
            added_one_week = parse_of_date(line_1) + timedelta(weeks=1)
            print(f'If we want to add one week to date {parse_of_date(line_1)} so it will be {added_one_week}')

            line_2 = getting_line_from_text(2, lines)
            current_day = datetime.strftime(parse_of_date(line_2), '%A')
            print(f'Name of day from date {parse_of_date(line_2)} is: {current_day}')

            line_3 = getting_line_from_text(3, lines)
            res = datetime.now() - parse_of_date(line_3)
            print(f'Date {parse_of_date(line_3)} was {res.days} days ago from current date')

            for line in filter(lambda x: not x.startswith(('1', '2', '3')), lines):
                print(f'Operation for line #{line} is not supported yet')

    except FileNotFoundError as e:
        print(f"{e}: File was not found!")


using_dates_from_file('data.txt')
