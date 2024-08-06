import datetime

input_date = "Jan 15, 2023 - 12:05:33"

date_py = datetime.datetime.strptime(input_date, '%b %d, %Y - %H:%M:%S')
date_not_py = datetime.datetime.strftime(date_py, '%d.%m.%Y, %H:%M')

print(date_py.strftime('%B'))
print(date_not_py)
