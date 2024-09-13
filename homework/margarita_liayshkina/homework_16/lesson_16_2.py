from datetime import datetime


def input_date():
    date_birth = input("Enter date birthday: ")

    try:
        date_input = datetime.strptime(date_birth, "%d.%m.%Y")
        age = (datetime.now() - date_input).days

        print(f"Your age in days: {age}")

    except ValueError :
        print("Error! Please enter your date birthday in the format: dd.mm.yyyy")


input_date()
