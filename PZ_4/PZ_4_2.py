# Даны целые положительные числа N и K. Используя только операции сложения и вычитания,
# найдите частное от деления нацело N на K, а также остаток от этого деления.

division = 0

while True:
    try:
        N, K = map(int, input("Введите два числа N и K: ").split())
        break
    except ValueError:
        print('Вы ввели не число или не 2 числа!')

while N - K >= 0:
    N -= K
    division += 1

print(f'Частное от деления N на K: {division}\nОстаток от деления: {N}')
