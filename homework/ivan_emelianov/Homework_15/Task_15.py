import os
from pathlib import Path


def open_file(file: str):

    rep_root = Path(os.path.dirname(__file__)).parent.parent.parent

    file_path = os.path.join(rep_root, 'homework', 'eugene_okulik', 'hw_15', f'{file}')

    with open(file_path, 'r', encoding='utf-8') as opened_file:
        data = opened_file.read()
        uppercase_latter = ''.join(filter(str.isupper, data))
        print(uppercase_latter)


open_file('data.txt')
