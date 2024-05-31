from computer import Computer
from human import Man, Woman, Human


comp = Computer('HP', 'Intel', '4 GB')
comp.save('1.txt')
del comp

comp = Computer.load('1.txt')
print(comp.get_info())


h = Human('John', 20, 'Мужчина')
m = Man('Joe', 25)
w = Woman('Julia', 27)
print(h, m, w, sep='\n')
