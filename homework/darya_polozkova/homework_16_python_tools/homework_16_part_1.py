import os
import sys
from datetime import datetime, timedelta

root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
path = os.path.join(root, 'eugene_okulik', 'hw_16')
data = os.path.join(path, 'data.txt')
print(data)
separator = '\\' if sys.platform == 'windows' else '/'
# homework/eugeny_okulik/hw_16/data.txt
with open(data, encoding='utf-8') as opened_file:
    data = opened_file.read()
    print(data)

dates = []

blocks = data.splitlines()

for block in blocks:
    content = block.split(' -')
    date_and_time = content[0][3:30]
    date = dates.append(date_and_time)
print(f'This is final list of dates: {dates}')

# 1. 2023-11-27 20:34:13.212967 - распечатать эту дату, но на неделю позже.
# Должно получиться 2023-12-04 20:34:13.212967
date_1 = dates[0]
date_1_to_python = datetime.strptime(date_1, '%Y-%m-%d %H:%M:%S.%f')
week = timedelta(days=7)
in_a_week = date_1_to_python + week
print(in_a_week)

# 2. 2023-07-15 18:25:10.121473 - распечатать какой это будет день недели
date_2 = dates[1]
day_2_to_python = datetime.strptime(date_2, '%Y-%m-%d %H:%M:%S.%f')
day_of_a_week = day_2_to_python.strftime('%A')
print(day_of_a_week)

# 3. 2023-06-12 15:23:45.312167 - распечатать сколько дней назад была эта дата
now = datetime.now()
date_3 = dates[2]
day_3_to_python = datetime.strptime(date_3, '%Y-%m-%d %H:%M:%S.%f')
ago = (now - day_3_to_python).days
print(f'This was {ago} days ago')
