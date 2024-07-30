results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]


def extract_and_add_10(line):
    return int(line.split()[-1]) + 10


for result in results:
    print(extract_and_add_10(result))
