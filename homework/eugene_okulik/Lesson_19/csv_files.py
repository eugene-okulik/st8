import csv


with open('data.csv', encoding='utf-8', newline='') as csv_file:
    file_data = csv.reader(csv_file)
    for line in file_data:
        print(line)


with open('data.csv', encoding='utf-8', newline='') as csv_file2:
    file_data2 = csv.DictReader(csv_file2)
    # for line in file_data2:
    #     print(line)
    data = list(file_data2)


print(data)
