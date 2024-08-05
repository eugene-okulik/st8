#   Jan 15, 2023 - 12:05:33
#   2023-01-15 12:05:33
import datetime
my_date = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')
print(python_date.strftime('%B'))

# Распечатайте дату в таком формате: "15.01.2023, 12:05"
print(python_date.strftime('%d.%m.%Y, %H:%M'))
