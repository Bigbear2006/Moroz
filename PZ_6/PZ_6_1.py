# Дан список ненулевых целых чисел размера N.
# Проверить, образуют ли его элементы геометрическую прогрессию.
# Если образуют, то вывести знаменатель прогрессии, если нет вывести 0.

while True:
    try:
        numbers = list(map(float, input("Введите список чисел: ").split()))
        break
    except ValueError:
        print('Вы ввели не список чисел!')

denominators = [numbers[index + 1] / num for index, num in enumerate(numbers[:-1])]

if denominators.count(denominators[0]) == len(denominators):
    print(f'Знаменатель прогрессии равен {denominators[0]}')
else:
    print(0)
