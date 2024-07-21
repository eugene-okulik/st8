"""
Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте
“Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim
vitae libero” и после этого выводит получившийся текст на экран.
Знаки препинания не должны оказаться внутри слова.
Если после слова идет запятая или точка, этот знак препинания должен идти после того же слова, но уже преобразованного.
"""

text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel." \
       " Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
words = text.split()
new_words = []

for word in words:
    if word[-1] in [",", "."]:
        word = word[:-1] + "ing" + word[-1]
    else:
        word = word + "ing"
    new_words.append(word)

new_text = ' '.join(new_words)
print(new_text)

# второе решение( Я видео почти досмотрел:) )
words = text.split()
new_words = []

for word in words:
    if word.endswith((",", ".")):
        word = word[:-1] + "ing" + word[-1]
    else:
        word = word + "ing"
    new_words.append(word)

new_text = ' '.join(new_words)
print(new_text)
