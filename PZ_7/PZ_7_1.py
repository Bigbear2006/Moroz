# Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами (одним или несколькими).
# Найти количество слов, которые содержат ровно три буквы «А».

string = input('Введите строку: ')
print([i.count('A') == 3 for i in string.split()].count(True))