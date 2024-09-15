import os
from pathlib import Path


class FileAnalyzer:
    def __init__(self, dir_path, search_text):
        self.dir_path = dir_path
        self.search_text = search_text
        self.repository_root = Path(os.path.dirname(__file__)).parent.parent.parent
        self.target_folder = os.path.join(self.repository_root, dir_path)

    @property
    def list_of_files(self):
        return os.listdir(self.target_folder)

    @staticmethod
    def read_file(file):
        with open(file, 'r', encoding='utf8') as opened_file:
            return opened_file.read()

    def search_text_in_file(self, file):
        text_was_found = False
        opened_file = self.read_file(file)
        print(f'Searching text: "{self.search_text}" in file "{file}"')
        print('.' * 50)

        for line_number, line in enumerate(opened_file.splitlines(), start=1):
            if self.search_text in line:
                text_was_found = True
                words = line.split()
                target_phrase = self.search_text.split()
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

    def analyze_files(self):
        for file in self.list_of_files:
            full_path = os.path.join(self.target_folder, file)
            self.search_text_in_file(full_path)


def main():
    dir_path = input('Pleas, enter path to folder: ')
    search_text = input('Please, enter needed text: ')
    analyzer = FileAnalyzer(dir_path, search_text)
    analyzer.analyze_files()


if __name__ == "__main__":
    main()
