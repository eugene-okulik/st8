with open('options.txt', encoding='utf-8') as options_file:
    data = options_file.read()

features = {}

blocks = data.split('\n\n')

for block in blocks:
    content = block.splitlines()
    # key, value = content[0], content[1:]
    key, *value = content
    features[key] = value

print(features)
