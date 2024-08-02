"""Map, filter
Есть такой список:

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30,
32, 30, 28, 24, 23]
С помощью функции map или filter создайте из этого списка новый список с жаркими днями. Будем считать жарким всё,
что выше 28.

Распечатайте из нового списка самую высокую температуру самую низкую и среднюю."""

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]


def hot_days_list(temp: list):
    hot_days = []
    for i in temp:
        if i > 28:
            hot_days.append(i)

    return hot_days


def temp_grade():
    temps = hot_days_list(temperatures)
    lowest = min(temps)
    maximum = max(temps)
    sorted_temps = sorted(temps)
    parity = len(sorted_temps)

    if parity % 2 == 1:
        median_temperature = sorted_temps[parity // 2]
    else:
        median_temperature = (sorted_temps[parity // 2 - 1])

    print(lowest)
    print(median_temperature)
    print(maximum)


temp_grade()
