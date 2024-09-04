import os
from pathlib import Path


file_dir = Path(os.path.dirname(__file__))
print(file_dir)
repository_root = file_dir.parent.parent
print(repository_root)
eugene_path = os.path.join(repository_root, 'eugene_okulik', 'hw_15')
print(eugene_path)
eugene_file = os.path.join(eugene_path, 'data.txt')
with open(eugene_file, encoding='utf-8') as opened_file:
    read_file_data = opened_file.read()

for one_symbol in read_file_data:
    if one_symbol.isupper():
        print(one_symbol)
