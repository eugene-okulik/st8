text1 = 'результат операции: 42'
text2 = 'результат операции: 514'
text3 = 'результат работы программы: 9'

text_pos = text1.find(':')
text_pos2 = text2.index(':')
text_pos3 = text3.index(':')

start_number1 = text_pos + 2
number_str1 = text1[start_number1:]
number1 = int(number_str1)
result1 = number1 + 10

start_number2 = text_pos2 + 2
number_str2 = text2[start_number2:]
number2 = int(number_str2)
result2 = number2 + 10

start_number3 = text_pos3 + 2
number_str3 = text3[start_number3:]
number3 = int(number_str3)
result3 = number3 + 10

print(result1)
print(result2)
print(result3)
