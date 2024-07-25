import random


def return_random():
    random_text = random.choice(["результат операции: ", "результат работы программы: "])
    rand_int = random.randint(1, 100)
    result = f"{random_text}{rand_int}"

    number_int = int(result.split(":")[1].strip()) + 10
    print(f"{random_text}{number_int}")


return_random()
