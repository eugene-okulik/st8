from math import sqrt

a = 1
b = 2

hupo = round(sqrt((a ** 2) + (b ** 2)), 2)
square = (a * b) / 2

print(f"Первый катет: {a}, второй катет: {b}")
print(f"Гипотенуза треугольника с указанными катетами: {hupo}")
print(f"Площадь треугольника с указанными катетами: {square}")
