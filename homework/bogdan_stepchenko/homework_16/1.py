import os
from pathlib import Path
from datetime import datetime, timedelta


def parse_of_date(line: str) -> datetime:
    date_str = ' '.join(line.split()[1:3])
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")


def using_dates_from_file(file: str):

    repository_root = Path(os.path.dirname(__file__)).parent.parent.parent
    target_file = os.path.join(repository_root, 'homework', 'eugene_okulik', 'hw_16', file)
    try:
        with open(target_file, 'r', encoding='utf-8') as opened_file:
            data = opened_file.read()
            lines = data.splitlines()

            for line in lines:
                formatted_date = parse_of_date(line)
                if line[0] == '1':
                    added_one_week = formatted_date + timedelta(weeks=1)
                    print(f'If we want to add one week to date {formatted_date} so it will be {added_one_week}')
                elif line[0] == '2':
                    current_day = datetime.strftime(formatted_date, '%A')
                    print(f'Name of day from date {formatted_date} is: {current_day}')
                elif line[0] == '3':
                    res = datetime.now() - formatted_date
                    print(f'Date {formatted_date} was {res.days} days ago from current date')
                else:
                    raise NotImplementedError('Code is not supported yet')
    except FileNotFoundError as e:
        print(f"{e}: File was not found!")


using_dates_from_file('data.txt')
