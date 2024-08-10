import datetime


date = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(date, '%b %d, %Y - %H:%M:%S')
#1. Распечатайте полное название месяца из этой даты
month = python_date.strftime('%B')
print(month)
#2. Распечатайте дату в таком формате: "15.01.2023, 12:05"
formated_time = python_date.strftime('%d.%m.%Y, %I:%M')
print(formated_time)
