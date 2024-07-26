str1 = 'результат операции: 4200'
str2 = 'результат операции: 514'
str3 = 'результат работы программы: 900'


def add10(text):
    place = text.find(':')
    number = text[place + 2:]
    number = int(number)
    result = number + 10
    print(result)


add10(str1)
add10(str2)
add10(str3)
