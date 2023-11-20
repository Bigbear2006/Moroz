# Составить функцию, которая выведет на экран сроку, содержащую задаваемое число символов.
import random
import string

while True:
    try:
        symbols_count = int(input("Введите Количество символов: "))
        break
    except ValueError:
        print('Вы ввели не число!')


def log(count: int):
    print(*random.sample(string.ascii_letters, count), sep='')


log(symbols_count)
