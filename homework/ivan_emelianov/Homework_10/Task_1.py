temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]


def max_temp(temp):
    if temp >= 28:
        return True
    else:
        return False


max_temp_list = list(filter(max_temp, temperatures))
print(max_temp_list)

middle_max_temp = sum(max_temp_list) / len(max_temp_list)

print(f'Самая высокая температура: {max(max_temp_list)}')
print(f'Самая высокая температура: {min(max_temp_list)}')
print(f'Самая высокая температура: {round(middle_max_temp, 1)}')
