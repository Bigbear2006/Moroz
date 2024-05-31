import os

# task 1
os.chdir('../PZ_11')
print(*filter(lambda x: not os.path.isdir(x), os.listdir()))

# task 2
os.chdir('..')
if not os.path.exists('test'):
    os.makedirs('test/test1')
# os.replace('PZ_6/1.txt', 'test/1.txt')
# os.replace('PZ_6/2.txt', 'test/2.txt')
# os.replace('PZ_7/1.txt', 'test/test1/1.txt')
# os.rename('test/test1/1.txt', 'test/test1/test.txt')
print(f"Размер файла test/1.txt {os.path.getsize('test/1.txt')}")
print(f"Размер файла test/2txt {os.path.getsize('test/2.txt')}")

# task 3
os.chdir('PZ_11')
print(min([os.path.basename(i) for i in os.listdir()], key=len))

# task 4
os.chdir('../reports')
# os.startfile('PZ_2.pdf')

# task 5
os.chdir('..')
os.remove('test/test1/test.txt')

