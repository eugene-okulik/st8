import gmpy2

"""Последовательность чисел Фибоначчи определяется формулой Fn = Fn-1 + Fn-2 .
 То есть, следующее число получается как сумма двух предыдущих. Первые два числа равны 1 , затем 2(1+1) ,
  затем 3(1+2) , 5(2+3) и так далее: 1, 1, 2, 3, 5, 8, 13, 21."""

"""Напишите функцию-генератор, которая генерирует список чисел фибоначчи
Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число"""


def fib_generator():
    f1, f2 = gmpy2.mpz(1), gmpy2.mpz(1)  # Использование gmpy2 для работы с большими числами
    yield f1
    yield f2
    while True:
        fn = f1 + f2
        yield fn
        f1, f2 = f2, fn


def print_specific_elements(generator, indices):
    current_index = 1
    next_index = indices.pop(0) if indices else None

    for value in generator:
        if current_index == next_index:
            print(f"The element at position {current_index} is {value}")
            next_index = indices.pop(0) if indices else None
            if next_index is None:
                break
        current_index += 1


indices_to_print = [5, 1000, 100000]
fib_gen = fib_generator()

print_specific_elements(fib_gen, indices_to_print)
