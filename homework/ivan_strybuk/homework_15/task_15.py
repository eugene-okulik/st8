import os
from pathlib import Path

file_dir = Path(os.path.dirname(__file__))
repository_root = file_dir.parent.parent.parent
eugene_okulik = os.path.join(repository_root, 'homework', 'eugene_okulik', 'hw_15')
eugene_file = os.path.join(eugene_okulik, 'data.txt')

with open(eugene_file, 'r', encoding='utf-8') as opened_file:
    for symbol in opened_file:
        if symbol[0].isupper():
            print(symbol[0])
        else:
            continue
