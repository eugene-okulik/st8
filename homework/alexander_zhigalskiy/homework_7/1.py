text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, "
        "facilisis vitae semper at, dignissim vitae libero.")

punctuation = [',', '.']

result = []

words = text.split()

for word in words:
    if word[-1] in punctuation:
        new_word = word[:-1] + 'ing' + word[-1]
    else:
        new_word = word + 'ing'
    result.append(new_word)

new_text = ' '.join(result)

print(new_text)
