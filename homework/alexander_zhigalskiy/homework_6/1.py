text1 = 'результат операции: 42'
text2 = 'результат операции: 514'
text3 = 'результат работы программы: 9'

text1_start = text1.find(':')
text1_result = int(text1[text1_start + 1:]) + 10

text2_start = text2.find(':')
text2_result = int(text2[text2_start + 1:]) + 10

text3_start = text3.index(':')
text3_result = int(text3[text3_start + 1:]) + 10

print(f'result1 = {text1_result} , result2 = {text2_result} , result3 = {text3_result}')
