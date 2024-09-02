"""
Попросите пользователя ввести дату рождения и попробуйте преобразовать дату в формат питона.
 В случае, если пользователь не угадал с форматом ввода даты, вы получите исключение.
 Обработайте это исключение и подскажите пользователю в каком формате нужно вводить дату.
 А когда пользователь введет дату правильно, скажите ему его возраст в днях.
"""

from datetime import datetime


def parse_date():
    date_str = input("Введите вашу дату рождения: ")

    try:
        birth_date = datetime.strptime(date_str, "%Y-%m-%d")

        current_date = datetime.now()
        age_in_days = (current_date - birth_date).days
        print(f"Ваш возраст в днях: {age_in_days}")

    except (EncodingWarning, ValueError, EOFError, SyntaxError) as err:
        print(err)


parse_date()
