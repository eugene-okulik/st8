import os
# import sys


dir_path = os.path.dirname(__file__)
print(dir_path)
file_path = os.path.join(dir_path, 'data.txt')
print(file_path)
# separator = '\\' if sys.platform == 'windows' else '/'
# /home/eugene/projects/st8/homework/eugene_okulik/Lesson_15/data.txt
# /Users/eugene/projects/st8/homework/eugene_okulik/Lesson_15
# C:\Users\eugene\projects\st8\homework\eugene_okulik/data.txt
with open(file_path, 'r', encoding='utf-8') as opened_file:
    data = opened_file.read()

print(data)
