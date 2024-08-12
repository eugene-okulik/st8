full_text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel.\n"
             "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero.")

words = full_text.split()
ls_text = []

for word in words:
    if word.endswith(','):
        new_word = word[:-1] + 'ing' + ','

    elif word.endswith('.'):
        new_word = word[:-1] + 'ing' + '.'

    else:
        new_word = word + 'ing'

    ls_text.append(new_word)

new_text = ' '.join(ls_text)
print(new_text)
