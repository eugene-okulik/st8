import os
from pathlib import Path
import argparse


class FileAnalyzer:
    def __init__(self):
        self.repository_root = Path(os.path.dirname(__file__)).parent.parent.parent

    @staticmethod
    def list_of_files(target_folder):
        files = os.listdir(target_folder)
        if not files:
            print(f"Directory {target_folder} does not have files!")
        else:
            return files

    @staticmethod
    def read_file(file):
        try:
            with open(file, 'r', encoding='utf8') as opened_file:
                return opened_file.read()
        except (FileNotFoundError, IOError) as error:
            print(f'Next error was occurred: {error}')
            return ""

    def search_text_in_file(self, file, search_text):
        text_was_found = False
        opened_file = self.read_file(file)
        print(f'Searching text: "{search_text}" in file "{file}"')
        print('.' * 50)

        for line_number, line in enumerate(opened_file.splitlines(), start=1):
            if search_text in line:
                text_was_found = True
                words = line.split()
                target_phrase = search_text.split()
                target_phrase_len = len(target_phrase)

                indexes = filter(
                    lambda el: words[el: el + target_phrase_len] == target_phrase, range(len(words))
                )
                for i in indexes:
                    start = max(i - 5, 0)
                    end = min(i + 6, len(words))
                    surrounding_words = ' '.join(words[start:end])
                    print(f'Needed text was found in file: "{file}"!')
                    print(f'Line number: {line_number}')
                    print(f'Slice of line with found text: "{surrounding_words}"')
                    print(' ' * 50)
        if not text_was_found:
            print(f'Needed text WAS NOT found in file {file}!')
            print(' ' * 50)

    def analyze_files(self, dir_path, search_text):
        target_folder = os.path.join(self.repository_root, dir_path)
        if not os.path.exists(target_folder):
            raise ValueError(f"Directory {target_folder} does not exist.")
        else:
            for file in self.list_of_files(target_folder):
                full_path = os.path.join(target_folder, file)
                self.search_text_in_file(full_path, search_text)


def main():
    parser = argparse.ArgumentParser(description="Search text in files inside directory")
    parser.add_argument('dir_path', help='Path to folder with files')
    parser.add_argument('search_text', help='Text which should be found in files')
    args = parser.parse_args()

    analyzer = FileAnalyzer()
    analyzer.analyze_files(args.dir_path, args.search_text)


if __name__ == "__main__":
    main()
