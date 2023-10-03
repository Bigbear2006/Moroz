#  Дано трёхзначное число. В нём зачеркнули первую слева цифру и приписали её справа. Вывести

while True:
    try:
        number = int(input("Введите трёхзначное число: "))
        break
    except ValueError:
        print('Вы ввели не число!')

first = number // 100
second = number // 10 % 10
third = number % 10

output = second * 100 + third * 10 + first
print(f'Вы ввели число {number}. Вывод: {output}')
