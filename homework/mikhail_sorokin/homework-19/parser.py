from argparse import ArgumentParser
import os
import re

parser = ArgumentParser(description="Search for a term in log files within a directory.")
parser.add_argument("directory", help="Directory containing log files")
parser.add_argument("--text", "-t", required=True, help="Value to search in the log files")
args = parser.parse_args()

directory_path = args.directory
search_term = args.text

if not os.path.exists(directory_path):
    print(f"Directory '{directory_path}' not found.")
elif not os.path.isdir(directory_path):
    print(f"'{directory_path}' is not a valid directory.")
else:
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as opened_file:
                    for line_number, line in enumerate(opened_file, 1):
                        if search_term in line:
                            words = re.findall(r'\S+', line)

                            try:
                                search_index = words.index(search_term)
                            except ValueError:
                                continue

                            start_index = max(search_index - 5, 0)
                            end_index = min(search_index + 5, len(words))
                            context = ' '.join(words[start_index:end_index])

                            # Выводим результат
                            print(f"Found in file '{file_path}', line {line_number}:")
                            print(f"... {context} ...")

            except Exception as e:
                print(f"An error occurred while reading the file '{file_path}': {e}")
