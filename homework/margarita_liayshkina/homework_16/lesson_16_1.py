import os
from pathlib import Path
from datetime import datetime, timedelta


try:
    file_dir = Path(os.path.dirname(__file__))
    repository_root = file_dir.parent.parent

    eugene_path = os.path.join(repository_root, 'eugene_okulik', 'hw_16')
    eugene_file = os.path.join(eugene_path, 'data.txt')

    with open(eugene_file, encoding='utf-8') as opened_file:
        read_file_data = opened_file.readlines()
        print(read_file_data)

except FileNotFoundError as error:
    print(f"Error: {error}")

finally:
    print("Finished checking file paths.")


for line in read_file_data:
    components = line.split(" - ")
    numbered_dates = components[0]
    date_str = numbered_dates.split(". ")[1].strip()
    date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

    if line == read_file_data[0]:
        new_date = date_obj + timedelta(weeks=1)
        print("First lesson:", new_date)

    elif line == read_file_data[1]:
        day_of_week = date_obj.strftime('%A')
        print("Second lessin:", day_of_week)

    elif line == read_file_data[2]:
        today = datetime.now()
        days_ago = (today - date_obj).days
        print("Tthird lesson:", days_ago, "days ago")
