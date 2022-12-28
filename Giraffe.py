from Animal import *


class Giraffe(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'ПППФФФФФФФ'
        self._animal_type = 'Жираф'
        self._biome = 'Пустыня'
        self._predator = False
        self._area = 20
        self._food = ['Трава', 'Колючки']