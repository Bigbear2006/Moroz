# Создайте класс "Компьютер" с атрибутами "марка", "процессор" и "оперативная
# память". Напишите метод, который выводит информацию о компьютере в формате
# "Марка: марка, Процессор: процессор, Оперативная память: память".

# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате.

import pickle


class Computer:
    def __init__(self, brand, processor, ram):
        self.brand = brand
        self.processor = processor
        self.ram = ram

    def __str__(self):
        return self.get_info()

    def get_info(self):
        return f'Марка {self.brand}, процессор {self.processor}, оперативная память {self.ram}'

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, filename):
        with open(filename, 'rb') as f:
            instance = pickle.load(f)
        return instance
