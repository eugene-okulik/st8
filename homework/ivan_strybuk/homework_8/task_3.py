"""
Получите из каждой строки с результатом число, прибавьте к полученному числу 10, результат сложения распечатайте:

результат операции: 42
результат операции: 54
результат работы программы: 209
результат: 2
"""
texts = ['результат операции: 42', 'результат операции: 54', 'результат работы программы: 209', 'результат: 2']
summand_value = 10


def parsers(text: [list, set]) -> None:
    for string in text:
        value_in_text = string[string.find(":") + 2::]
        total_amount = int(value_in_text) + summand_value
        print(total_amount)


parsers(texts)


#  version_2 короткая
# def parser(text: str) -> int: return int(text.split()[-1]) + summand_value
def parser(text: str) -> int:
    return int(text.split()[-1]) + summand_value


# These "asserts" are used for self-checking
assert parser("результат операции: 42") == 52
assert parser("результат операции: 54") == 64
assert parser("результат работы программы: 209") == 219
assert parser("результат: 2") == 12
