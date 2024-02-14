# В матрице найти отрицательные элементы, сформировать из них новый массив.
# Вывести размер полученного массива.
import random

matrix = [
    [random.randint(-10, 10) for _ in range(5)]
    for _ in range(5)
]

negative = [j for i in matrix for j in i if j < 0]
print(f'Количество нечетных элементов: {len(negative)}')
