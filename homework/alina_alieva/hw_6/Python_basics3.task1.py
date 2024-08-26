str1 = 'результат операции: 42'
str2 = 'результат операции: 514'
str3 = 'результат работы программы: 9'

number1 = str1.index(':') + 1
number2 = str2.index(':') + 1
number3 = str3.index(':') + 1

my_num1 = int(str1[number1:])
print(my_num1 + 10)
my_num2 = int(str2[number2:])
print(my_num2 + 10)
my_num3 = int(str3[number3:])
print(my_num3 + 10)
