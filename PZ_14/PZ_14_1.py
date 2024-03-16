# В исходном текстовом файле(Dostoevsky.txt) найти все годы деятельности писателя
# (например, 1821 года, 1837 год, 1843 году и так далее по всему тексту). Посчитать
# количество полученных элементов.

import re

with open('Dostoevsky.txt', 'r') as f:
    data = f.read()

years = re.findall(r"(?:[0-9]{4}–)?[0-9]{4}\s?(?:год.?|гг?\.)", data)
print(f'Найденные даты: {years}')
print(f'Найдено дат: {len(years)}')
