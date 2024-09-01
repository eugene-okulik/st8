import os
import sys

root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
path = os.path.join(root, 'eugene_okulik', 'Lesson_15')
data = os.path.join(path, 'data.txt')
print(data)
separator = '\\' if sys.platform == 'windows' else '/'
# homework/eugene_okulik/hw_15/data.txt
with open(data, encoding='utf-8') as opened_file:
    data = opened_file.read()
    uppercase_letters = list(filter(lambda char: char.isupper(), ''.join(data)))
    print(uppercase_letters)
