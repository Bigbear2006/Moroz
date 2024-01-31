# Из предложенного текстового файла (text18-24.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив символы нижнего
# регистра на верхний.

import re

with open('text18-24.txt', 'r', encoding='utf-16') as f:
    content = f.read()

letters_count = len(re.sub(r'[^А-Яа-я]', '', content))
print(f'Содержимое файла:\n{content}\n\nКоличество букв: {letters_count}')

with open('text18-24-upper.txt', 'w', encoding='utf-16') as f:
    f.write(content.upper())
