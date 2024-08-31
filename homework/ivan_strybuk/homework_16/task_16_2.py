from datetime import datetime

while True:
    try:
        date = str(input('Введите дату рождения в формате (Format:dd mm yyyy): \n'))
        date = datetime.strptime(date, "%d %m %Y")
        print(f'Ваш возраст {(datetime.now() - date).days} дней')
        break
    except ValueError:
        print('Введен неверный формат даты')
