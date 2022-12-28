class Animal:

    def __init__(self, name, volume_of_food, age):
        self.name = name
        self._volume_of_food = volume_of_food
        self.age = age
        self._food = []
        self.sound = ''
        self._animal_type = ''
        self._biome = ''
        self._satiety = 0
        self._area = ''
        self._predator = bool
        self.animal_is_full = bool

    def play(self):
        print(self.name, ': Я поиграл')

    def sound_animal(self):
        print(self.name, ':', self.sound)

    def eat(self, value, food):
        if self._satiety + value == self._volume_of_food and food in self._food:
            print(self.name, ': Я наелся')
            self.animal_is_full = True
        elif self._satiety + value > self._volume_of_food and food in self._food:
            print(self.name, ': Я объелся, у меня осталась', self._satiety + value - self._volume_of_food, self._food)
            self.animal_is_full = True
        elif food in self._food:
            print(self.name, ': Я не наелся, дай мне еще', self._volume_of_food - (self._satiety + value), self._food)
            self._satiety += value
        else:
            print(self.name, ': Шо ты мне дал, я такого не ем')

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


class Elefant(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'УУХХЕРРРРРРРРРРРРРРРРРР'
        self._animal_type = 'Слон'
        self._biome = 'Пустыня'
        self._predator = False
        self._area = 15
        self._food = ['Трава', 'Бананы']


class Tiger(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'РРРРРР'
        self._animal_type = 'Тигр'
        self._biome = 'Равнина'
        self._predator = True
        self._area = 10
        self._food = ['Мясо', 'Рыба']


class Pinguin(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'Хрю'
        self._animal_type = 'Пингвин'
        self._biome = 'Тундра'
        self._predator = True
        self._area = 5
        self._food = ['Рыба', 'Анчоусы']


class Dog(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'Гав'
        self._animal_type = 'Собака'
        self._biome = 'Тундра'
        self._predator = True
        self._area = 3
        self._food = ['Корм', 'Мясо']


class Wolf(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'РРРРРР'
        self._animal_type = 'Волк'
        self._biome = 'Равнина'
        self._predator = True
        self._area = 3
        self._food = ['Рыба', 'Мясо']


class Giraffe(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'ПППФФФФФФФ'
        self._animal_type = 'Жираф'
        self._biome = 'Пустыня'
        self._predator = False
        self._area = 20
        self._food = ['Трава', 'Бананы']


class Goat(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'МЕЕЕЕЕЕЕ'
        self._animal_type = 'Козел'
        self._biome = 'Равнина'
        self._predator = False
        self._area = 10
        self._food = ['Трава', 'Колючки']
