import os
from pathlib import Path


def print_only_upper_letters(file: str):

    repository_root = Path(os.path.dirname(__file__)).parent.parent.parent

    target_file = os.path.join(repository_root, 'homework', 'eugene_okulik', 'hw_13', f'{file}')

    with open(target_file, 'r', encoding='utf-8') as opened_file:
        res = ''
        data = opened_file.read()
        for i in data:
            if i.isupper():
                res += i
        print(f'Only upper letters from file data.txt: {res}')


print_only_upper_letters('data.txt')
