from datetime import datetime

while True:
    try:
        birthday = input('When is your birthday? ')
        date = datetime.strptime(birthday, "%d %m %Y")
        print(f'Your age is {(datetime.now() - date).days} days')
        break
    except (ValueError, SyntaxError) as err:
        print('Please enter birthday in format %d %m %Y')
