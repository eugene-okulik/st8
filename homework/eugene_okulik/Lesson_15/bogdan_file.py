import os
from pathlib import Path


# repository_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
file_dir = Path(os.path.dirname(__file__))
repository_root = file_dir.parent.parent.parent
print(repository_root)
bogdan_path = os.path.join(repository_root, 'homework', 'bogdan_stepchenko')
print(bogdan_path)
bogdan_file = os.path.join(bogdan_path, 'file.txt')

with open(bogdan_file, encoding='utf-8') as opened_file:
    print(opened_file.read())
