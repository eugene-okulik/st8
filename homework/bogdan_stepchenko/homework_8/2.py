# Задание №2
# Дан такой словарь:
#
# words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
# Выведите на экран каждый ключ столько раз сколько указано в значении. Т.е. как-то так:
#
# III
# lovelovelovelove
# итд
# Cделайте так, чтобы каждый ключ печатался в одной строке (как в примере)


words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def print_key_from_dict(dictionary: dict):
    for k, v in dictionary.items():
        print(k * v)


print_key_from_dict(words)
