# Задание №1
# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в
# тексте “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at, dignissim vitae libero” и после
# этого выводит получившийся текст на экран. Знаки препинания не
# должны оказаться внутри слова. Если после слова идет запятая
# или точка, этот знак препинания должен идти после того же слова, но уже преобразованного.

sentence = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. " \
           "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

res = []
postfix = 'ing'

for word in sentence.split():
    if word.endswith('.') or word.endswith(','):
        res.append(word[:-1] + postfix + word[-1])
    else:
        res.append(word + postfix)

res = ' '.join(res)
print(res)
