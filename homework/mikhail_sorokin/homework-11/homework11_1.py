"""
Обработка даты
Дана такая дата: "Jan 15, 2023 - 12:05:33"

Преобразуйте эту дату в питоновский формат, после этого:

1. Распечатайте полное название месяца из этой даты

2. Распечатайте дату в таком формате: "15.01.2023, 12:05"
"""

import datetime

date = "Jan 15, 2023 - 12:05:33"

date_parse = datetime.datetime.strptime(date, '%b %d, %Y - %H:%M:%S')
python_date = datetime.datetime.fromisoformat(str(date_parse))
months_name = datetime.datetime.strftime(python_date, '%B')
full_date = datetime.datetime.strftime(python_date, '%d.%m.%Y, %H:%M')
print(months_name, full_date, sep="\n")
