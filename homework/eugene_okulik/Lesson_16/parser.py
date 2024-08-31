with open('options.txt', encoding='utf-8') as options_file:
    data = options_file.read()

features = {}

# lines = data.split('/n')
lines = data.splitlines()

print(lines)

new_categ = True
current_categ = None
for line in lines:
    if new_categ is True:
        features[line] = []
        current_categ = line
        new_categ = False
    elif line == '':
        new_categ = True
        current_categ = None
    else:
        features[current_categ].append(line)

print(features)
