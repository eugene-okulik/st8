import os
import sys
from pathlib import Path

file_dir = Path(os.path.dirname(__file__))
print(f'ETO{file_dir}')
root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(f'ETOO{root}')
path = os.path.join(root, 'eugene_okulik', 'hw_13')
print(path)
data = os.path.join(path, 'data.txt')
print(data)
separator = '\\' if sys.platform == 'windows' else '/'
# homework/eugene_okulik/hw_13/data.txt
with open(data, encoding='utf-8') as opened_file:
    data = opened_file.read()
    uppercase_letters = list(filter(lambda char: char.isupper(), ''.join(data)))
    print(uppercase_letters)
