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
    for FILE in logs:
        full_path = os.path.join(LOGS, FILE)
        with open(full_path, "r", encoding='utf-8') as opened_file:
            data = opened_file.readlines()
            for INDEX, line in enumerate(data, 1):
                if TEXT_FOR_SEARCH in line:
                    print(f"Found {TEXT_FOR_SEARCH} in log {FILE} on '{INDEX}' line.")

                    first_letter_index = line.index(TEXT_FOR_SEARCH)
                    last_letter_index = first_letter_index + len(TEXT_FOR_SEARCH)

                    start = first_letter_index - 50
                    end = last_letter_index + 51

                    if start < 0:
                        print(line[:end], '\n')
                    elif end > len(line):
                        print(line[start:], '\n')
                    else:
                        print(line[start:end], '\n')

    if not found:
        print(f'Nothing is found')


search(FILES_IN_DIR)
