text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
words = text.split(' ')
print(words)
new_words = []

for word in words:
    if word.endswith((",", ".")):
        word = word[:-1] + "ing" + word[-1]
    else:
        word = word + "ing"
    new_words.append(word)

new_text = ' '.join(new_words)
print(new_text)
