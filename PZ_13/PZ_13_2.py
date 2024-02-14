# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов.
import random

matrix = [
    [random.randint(-10, 10) for _ in range(5)]
    for _ in range(5)
]

averages = [sum(i) / len(i) for index, i in enumerate(matrix) if index % 2 != 0]
print(f'Среднее арифметическое элементов строк с нечетным номером: {averages}')
