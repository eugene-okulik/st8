def extract_num (result_line):
    number_index = int(result_line.split(":")[1].strip())
    new_number = number_index + 10
    return result_line.split(":")[0] + ": " + str(new_number)

data_number = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for line in data_number :
    print(extract_num(line))
