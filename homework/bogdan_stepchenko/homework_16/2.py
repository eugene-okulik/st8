from datetime import datetime


def age_in_days(age: str) -> int:
    formatted_date = datetime.strptime(age, "%Y-%m-%d")
    days = (datetime.now() - formatted_date).days
    return days


def ask_birth_date():
    while True:
        age = input('Please, enter your date of birth: ')
        try:
            print(f'Your age in days is: {age_in_days(age)}')
            break
        except ValueError as e:
            print(f'!!!Error!!!!\n{e}.\nCorrect one is: YYYY-MM-DD. Please, try again!')


ask_birth_date()
