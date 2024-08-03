""" Дана такая дата: "Jan 15, 2023 - 12:05:33"

Преобразуйте эту дату в питоновский формат, после этого:

1. Распечатайте полное название месяца из этой даты

2. Распечатайте дату в таком формате: "15.01.2023, 12:05"
"""
import datetime

my_date = "Jan 15, 2023 - 12:05:33"

python_date = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')

print(f"Полное название месяца: {"0" + str(python_date.date().month)}")
print(f"Полное название месяца: {python_date.strftime("%m")}")
print(f"Полное название месяца: {python_date.strftime("%b")}")
print(f"Полное название месяца: {python_date.strftime("%B")}")
print(f'Дата в таком формате "15.01.2023, 12:05": "{python_date.strftime("%d.%m.%Y, %H:%M")}"')
