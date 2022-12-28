from Animal import *


class Elefant(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'УУХХЕРРРРРРРРРРРРРРРРРР'
        self._animal_type = 'Слон'
        self._biome = 'Пустыня'
        self._predator = False
        self._area = 15
        self._food = ['Трава', 'Бананы']