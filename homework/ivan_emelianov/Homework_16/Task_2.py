from datetime import datetime


def date_birthday(date):

    try:
        date_birt = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.now()
        days_passed = (current_date - date_birt).days
        print(days_passed)
    except ValueError:
        print('Неверный формат даты. Используйте формат ГГГГ-ММ-ДД.')


date_birthday(input('Введите дату рождения: '))
