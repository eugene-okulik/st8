import datetime

total_data = "Jan 15, 2023 - 12:05:33"
python_data = datetime.datetime.strptime(total_data, "%b %d, %Y - %H:%M:%S")
human_data = python_data.strftime("%b %d, %Y - %H:%M:%S")
print(human_data)

month_full = python_data.strftime("%B")
print(month_full)

format_data_2 = "15.01.2023, 12:05"
python_data_2 = datetime.datetime.strptime(format_data_2, "%d.%m.%Y, %H:%M")
# print(python_data_2)
human_data_2 = python_data_2.strftime("%d.%m.%Y, %H:%M")
print(human_data_2)
