text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
text_set = text.split()
result = []
for add_ing in text_set:
    if add_ing[-1] in ',.':
        new_result = add_ing[:-1] + 'ing' + add_ing[-1]
    else:
        new_result = add_ing + 'ing'
    result.append(new_result)

final_result = ' '.join(result)
print(final_result)
