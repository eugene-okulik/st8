import os.path
import argparse
import sys

separator = '\\' if sys.platform == 'windows' else '/'
parser = argparse.ArgumentParser()
# positional argument
parser.add_argument("file", help="Type where to look for files")
# опциональный аргумент указывается через -- и булевый action="store_true"
parser.add_argument("-s", "--search", dest="search", help="type text for search")
args = parser.parse_args()
LOGS = args.file
TEXT_FOR_SEARCH = args.search
FILES_IN_DIR = os.listdir(LOGS)
# В итоге, пользователь сможет обратиться к программе (например, она будет у вас называться analyzer.py)
# таким образом: python analyzer.py C:\user\data\logs --text WARN


def search(logs):
    found = False
    for file in logs:
        full_path = os.path.join(LOGS, file)
        with open(full_path, "r", encoding='utf-8') as opened_file:
            data = opened_file.readlines()
            for data in enumerate(data):
                if TEXT_FOR_SEARCH in data[1]:
                    print(f"""Text: {TEXT_FOR_SEARCH} is found in {data[0]+1}""")
                    found = True
    if not found:
        print(f'Nothing is found')


search(FILES_IN_DIR)
