class Animal:

    def __init__(self, name, volume_of_food, age):
        self.name = name
        self.__volume_of_food = volume_of_food
        self.age = age
        self.sound = ''

    def play(self):
        print(self.name, ': Я поиграл')

    def sound_animal(self):
        print(self.name, ':', self.sound)

    def eat(self):
        print(self.name, 'Я ем', self.volume_of_food)

    @property
    def volume_of_food(self):
        return self.__volume_of_food


class Slon(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'УУХХЕРРРРРРРРРРРРРРРРРР'


class Tiger(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'РРРРРР'


class Pinguin(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'Хрю'

