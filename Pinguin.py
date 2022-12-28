from Animal import *


class Pinguin(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'Хрю'
        self._animal_type = 'Пингвин'
        self._biome = 'Тундра'
        self._predator = True
        self._area = 5
        self._food = ['Рыба', 'Анчоусы']