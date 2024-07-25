words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def word_repeat(dictionary):
    for key, value in dictionary.items():
        print(f"{key * value}")


def word_repeat2(dictionary):
    result = [key * value for key, value in dictionary.items()]
    for item in result:
        print(item)


def word_repeat3(dictionary):
    result = [key * value for key, value in dictionary.items()]
    list(map(print, result))


word_repeat(words)
word_repeat2(words)
word_repeat3(words)

list(map(word_repeat, [words]))
list(map(lambda item: print(item[0] * item[1]), words.items()))
