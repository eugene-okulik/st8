"""
С помощью функции map или filter создайте из этого списка новый список с жаркими днями.
Будем считать жарким всё, что выше 28.
Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.
"""

temperatures = ([20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34,
                 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23])

# filter функция
temperature_more_28 = list(filter(lambda temp: temp > 28, temperatures))

min_temp = min(temperature_more_28)
max_temp = max(temperature_more_28)
average_temp = round(sum(temperature_more_28) / len(temperature_more_28), 1)

print(f"Минимальная температура: {min_temp}")  # Минимальная температура: 29
print(f"Максимальная температура: {max_temp}")  # Максимальная температура: 34
print(f"Средняя температура: {average_temp}")  # Средняя температура: 31.1
print("-" * 10)

#  List comprehensions
temperature_above_28 = [int(item) for item in temperatures if item > 28]

min_temperature = min(temperature_above_28)
max_temperature = max(temperature_above_28)
median_temperature = round(sum(temperature_above_28) / len(temperature_above_28), 1)

print(f"Минимальная температура: {min_temperature}")  # Минимальная температура: 29
print(f"Максимальная температура: {max_temperature}")  # Максимальная температура: 34
print(f"Средняя температура: {median_temperature}")  # Средняя температура: 31.1
