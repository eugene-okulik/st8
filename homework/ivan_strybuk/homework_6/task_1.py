text = "результат операции: 42"
text_1 = "результат операции: 514"
text_2 = "результат работы программы: 9"
summand = 10

split_text = text[text.find(":") + 2::]
split_text_1 = text_1[text_1.find(":") + 2::]
split_text_2 = text_2[text_2.find(":") + 2::]

expression_0 = int(split_text) + summand
expression_1 = int(split_text_1) + summand
expression_2 = int(split_text_2) + summand

print(f"Есть текст '{text}'. К числу {split_text} + {summand} =", expression_0)
print(f"Есть текст '{text_1}'. К числу {split_text_1} + {summand} =", expression_1)
print(f"Есть текст '{text_2}'. К числу {split_text_2} + {summand} =", expression_2)

# def parser_number(some_pages: str) -> int:
#     number_to_add = 10
#     split_txt = some_pages.split(': ')[1]
#     expression = int(split_txt) + number_to_add
#     return expression
#
#
# print(parser_number("результат операции: 42") == 52)
# print(parser_number("результат операции: 514") == 524)
# print(parser_number("результат работы программы: 9") == 19)
