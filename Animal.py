class Animal:

    def __init__(self, name, volume_of_food, age):
        self.name = name
        self._volume_of_food = volume_of_food
        self.age = age
        self._food = []
        self.sound = ''
        self._animal_type = ''
        self._biome = ''
        self._area = ''
        self._satiety = 0
        self._predator = bool
        self.animal_is_full = bool

    def play(self):
        print(self.name, ': Я поиграл')

    def sound_animal(self):
        print(self.name, ':', self.sound)

    def eat(self, value, food):
        if self._satiety + value == self._volume_of_food and food in self._food:
            print(self.name, ': Я наелся')
            self._satiety += value
            self.animal_is_full = True
        elif self._satiety + value > self._volume_of_food and food in self._food:
            print(self.name, ': Я объелся, у меня осталась', self._satiety + value - self._volume_of_food, self._food)
            self._satiety += value
            self.animal_is_full = True
        elif food in self._food:
            print(self.name, ': Я не наелся, дай мне еще', self._volume_of_food - value, self._food)
            self._satiety += value
            self.animal_is_full = False
        else:
            print(self.name, ': Шо ты мне дал, я такого не ем')
            self.animal_is_full = False

    @property
    def volume_of_food(self):
        return self._volume_of_food

    @property
    def animal_type(self):
        return self._animal_type

    @property
    def food(self):
        return self._food

    @property
    def biome(self):
        return self._biome

    @property
    def predator(self):
        return self._predator

    @property
    def satiety(self):
        return self._satiety

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        if value >= 0:
            self._area = value
        else:
            print('Так нельзя')