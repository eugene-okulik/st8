# opened_file = open('data.txt', 'r', encoding='utf-8')
# data = opened_file.read()
# print(data.index('A'))
# opened_file.close()

with open('data.txt', 'r', encoding='utf-8') as opened_file:
    data = opened_file.read()
    # print(data.index('A'))

print(data)


with open('new_data.txt', 'w', encoding='utf-8') as opened_file:
    opened_file.write('BBBBBB')

with open('new_data.txt', 'w', encoding='utf-8') as opened_file:
    opened_file.write('BABABABABABA')

with open('new_data.txt', 'a', encoding='utf-8') as opened_file:
    opened_file.write('CCCCC')
