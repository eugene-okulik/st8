# срез

results = [
    "результат операции: 42",
    "результат операции: 514",
    "результат работы программы: 9"
]

str1 = "результат операции: 42"
str2 = "результат операции: 514"
str3 = "результат работы программы: 9"

print(int(str1[str1.find(':') + 2:]) + 10)
print(int(str2[str2.find(':') + 2:]) + 10)
print(int(str3[str3.find(':') + 2:]) + 10)