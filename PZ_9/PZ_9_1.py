# Дана строка 'груши 45 991 63 100 12 морковь 13 47 260 16', отражающая продажи продукции по дням в кг.
# Преобразовать информацию из строки в словари, с использованием функции найти минимальные продажи по
# каждому виду продукции, результаты вывести на экран.
import re

string = 'груши 45 991 63 100 12 морковь 13 47 260 16'

names = re.findall(r'[а-я]+', string)
sells = re.findall(r'[0-9\s]+', string)
sells = list(map(lambda x: x.split(), sells))

alls = {n: list(map(int, s)) for n, s in zip(names, sells)}
mins = {n: min(alls[n]) for n in names}
print(f'Минимальные продажи: {mins}')
