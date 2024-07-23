text_task = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel."
             " Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")

new_string = []
value = 'ing'

for text in text_task.split():
    if "," in text:
        new_string.append(text[:-1] + value[:] + text[-1])
    elif "." in text:
        new_string.append(text[:-1] + value[:] + text[-1])
    else:
        new_string.append(text[:] + value[:])

print(' '.join(new_string))
