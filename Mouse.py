from Animal import *


class Mouse(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = '3,14'
        self._animal_type = 'Мышь'
        self._biome = 'Равнина'
        self._predator = False
        self._area = 1
        self._food = ['Зерно', 'Трава']