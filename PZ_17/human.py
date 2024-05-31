# Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
# Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
# "Человек". Каждый класс должен иметь метод, который выводит информацию о
# поле объекта

class Human:
    def __init__(self, name, age, gender):
        if gender not in ('Мужчина', 'Женщина'):
            raise ValueError('gender must be "Мужчина" or "Женщина"')
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return self.get_info()

    def get_info(self):
        return f'{self.name}, {self.age} лет, {self.gender}'


class Man(Human):
    def __init__(self, name, age):
        super().__init__(name, age, 'Мужчина')


class Woman(Human):
    def __init__(self, name, age):
        super().__init__(name, age, 'Женщина')
