# Составить список, в который будут включены только согласные буквы и привести
# их к верхнему регистру. Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели',
# 'Каир'].
import re

consonants = r'[^бвгджзклмнпрстфхцчшщъь]'

lst = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
lst = list(map(lambda x: re.sub(consonants, '', x, flags=re.IGNORECASE), lst))
upper_lst = list(map(lambda x: x.upper(), lst))

print(upper_lst)
