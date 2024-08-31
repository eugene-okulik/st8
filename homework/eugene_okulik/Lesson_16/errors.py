def calc(x: str, y: str):
    try:
        x, y = int(x), int(y)
        print(x / y)
    # except ZeroDivisionError:
    #     print(f'Y is zero: x = {x}, y = {y}')
    # except ValueError:
    #     print(f'One of operands can not be converted to int: x = {x}, y = {y}')
    except (ZeroDivisionError, ValueError) as err:
        print(err)
        print(f'x = {x}, y = {y}')
        raise err


while True:
    a, b = input('number 1:'), input('number 2:')
    if b != '4321':
        calc(a, b)
    else:
        break
