from Animal import *


class Tiger(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'РРРРРР'
        self._animal_type = 'Тигр'
        self._biome = 'Равнина'
        self._predator = True
        self._area = 10
        self._food = ['Мясо', 'Рыба']