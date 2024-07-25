import random


# (number := int(input("Guess number: "))) == (target := random.randint(1, 10))
# Выше с моржом, но линтер такое решение не пропускает так как эти переменные типа не определенны
def try_to_guess_number():
    while True:
        guess = random.randint(1, 10)
        if int(input("Try to guess: ")) == guess:
            print("Congratulations! You guessed!")
            break
        else:
            print("This is not the correct number, try again.")


try_to_guess_number()


def good_luck(number):
    while True:
        guess = random.randint(1, 1000000)
        if number == guess:
            print("Congratulations! You guessed!")
            return True
        else:
            print("This is not the correct number, try again!")
            return False


def selector():
    while True:
        rand = random.randint(1, 1000000)
        if good_luck(rand) is True:
            break

# почему если тут сделать без is True то результат будет такой же ?
# Оператор if же не должен понимать когда условие выполнилось, а когда нет в таком случае


selector()
