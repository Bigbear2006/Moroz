# Дано четырехзначное число.
# Проверить истинность высказывания "Данное число читается одинаково слева направо и справа налево".

while True:
    try:
        number = int(input("Введите четырехзначное число: "))
        break
    except ValueError:
        print('Вы ввели не число!')

first = number // 1000
second = number // 100 % 10
third = number // 10 % 10
last = number % 10

if first == last and second == third:
    print(f'Число {number} читается одинаково слева направо и справа налево')
else:
    print(f'Число {number} НЕ читается одинаково слева направо и справа налево')
