# Описать функцию RectPS(x1, y1, x2, y2, P, S), вычисляющую периметр P и площадь S прямоугольника со сторонами,
# параллельными осям координат, по координатам (x1, y1), (x2, y2) его противоположных вершин
# (x1, y1, x2, y2 входные, Р и S выходные параметры вещественного типа).
# С помощью этой функции найти периметры и площадь прямоугольника с данными противоположными вершинами.

while True:
    try:
        x1, y1, x2, y2 = map(float, input("Введите 4 числа через пробел (x1, y1, x2, y2): ").split())
        break
    except ValueError:
        print('Вы ввели не число или не 4 числа!')


def rectPS(x1, y1, x2, y2):
    height = abs(x1 - x2)
    width = abs(y1 - y2)
    P = 2 * (height * width)
    S = height * width
    return P, S


P, S = rectPS(x1, y1, x2, y2)
print(f'P прямоугольника равен {P}.\nS прямоугольника равна {S}')
