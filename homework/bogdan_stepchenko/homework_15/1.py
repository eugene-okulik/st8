import os
from pathlib import Path


def print_only_upper_letters(file: str):

    repository_root = Path(os.path.dirname(__file__)).parent.parent.parent

    target_file = os.path.join(repository_root, 'homework', 'eugene_okulik', 'hw_13', f'{file}')

    with open(target_file, 'r', encoding='utf-8') as opened_file:
        data = opened_file.read()
        res = ''.join(filter(str.isupper, data))
        print(f'Only upper letters from file {file}: {res}')


print_only_upper_letters('data.txt')
