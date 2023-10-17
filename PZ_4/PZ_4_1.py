# Даны целые числа A и B (A > B). Вывести все целые числа от A до B включительно;
# при этом число A должно выводиться 1 раз, число A + 1 должно выводиться 2 раза и т. д.

while True:
    try:
        A, B = map(int, input("Введите два числа A и B (A < B): ").split())
        break
    except ValueError:
        print('Вы ввели не число или не 2 числа!')

for index, i in enumerate(range(A, B + 1)):
    print(' '.join([str(i)] * (index + 1)))
