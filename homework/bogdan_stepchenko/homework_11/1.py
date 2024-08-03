from datetime import datetime

# Дана такая дата: "Jan 15, 2023 - 12:05:33"
#
# Преобразуйте эту дату в питоновский формат, после этого:
#
# 1. Распечатайте полное название месяца из этой даты
#
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"

date = "Jan 15, 2023 - 12:05:33"

formatted_date = datetime.strptime(date, '%b %d, %Y - %X')
print(f'Formatted date: {formatted_date}')

current_month = formatted_date.strftime("Month: %B")
print(current_month)

reformatted_date = formatted_date.strftime("Reformatted date: %d.%m.%Y, %H:%m")
print(reformatted_date)
