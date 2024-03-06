# Создайте класс "Компьютер" с атрибутами "марка", "процессор" и "оперативная
# память". Напишите метод, который выводит информацию о компьютере в формате
# "Марка: марка, Процессор: процессор, Оперативная память: память".

class Computer:
    brand = None
    processor = None
    ram = None

    def __init__(self, brand, processor, ram):
        self.brand = brand
        self.processor = processor
        self.ram = ram

    def __str__(self):
        return self.get_info()

    def get_info(self):
        return f'Марка {self.brand}, процессор {self.processor}, оперативная память {self.ram}'


comp = Computer('HP', 'Intel', '4 GB')
print(comp.get_info())
