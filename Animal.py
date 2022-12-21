class Animal:

    def __init__(self, name, volume_of_food, food, age):
        self.name = name
        self._volume_of_food = volume_of_food
        self.age = age
        self._food = food
        self.sound = ''
        self._animal_type = ''
        self._biome = ''
        self._area = ''
        self._predator = bool
        self.eat_till_full = bool

    def play(self):
        print(self.name, ': Я поиграл')

    def sound_animal(self):
        print(self.name, ':', self.sound)

    def eat(self):
        print(self.name, ':', 'Я ем', self.volume_of_food, self.food)

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
    def area(self):
        return self._area

    @property
    def predator(self):
        return self._predator

    @area.setter
    def area(self, value):
        if value >= 0:
            self._area = value
        else:
            print('Так нельзя')


class Elefant(Animal):

    def __init__(self, name, volume_of_food, food, age):
        super().__init__(name, volume_of_food, food, age)
        self.sound = 'УУХХЕРРРРРРРРРРРРРРРРРР'
        self._animal_type = 'Слон'
        self._biome = 'Пустыня'
        self._predator = False
        self._area = 15


class Tiger(Animal):

    def __init__(self, name, volume_of_food, food, age):
        super().__init__(name, volume_of_food, food, age)
        self.sound = 'РРРРРР'
        self._animal_type = 'Тигр'
        self._biome = 'Равнина'
        self._predator = True
        self._area = 10


class Pinguin(Animal):

    def __init__(self, name, volume_of_food, food, age):
        super().__init__(name, volume_of_food, food, age)
        self.sound = 'Хрю'
        self._animal_type = 'Пингвин'
        self._biome = 'Тундра'
        self._predator = True
        self._area = 5


class Dog(Animal):

    def __init__(self, name, volume_of_food, food, age):
        super().__init__(name, volume_of_food, food, age)
        self.sound = 'Гав'
        self._animal_type = 'Собака'
        self._biome = 'Тундра'
        self._predator = True
        self._area = 3


class Sheep(Animal):

    def __init__(self, name, volume_of_food, food, age):
        super().__init__(name, volume_of_food, food, age)
        self.sound = 'БЕЕЕЕ'
        self._animal_type = 'Овца'
        self._biome = 'Горы'
        self._predator = False
        self._area = 8


class Wolf(Animal):

    def __init__(self, name, volume_of_food, food, age):
        super().__init__(name, volume_of_food, food, age)
        self.sound = 'РРРРРР'
        self._animal_type = 'Волк'
        self._biome = 'Равнина'
        self._predator = True
        self._area = 3


class Giraffe(Animal):

    def __init__(self, name, volume_of_food, food, age):
        super().__init__(name, volume_of_food, food, age)
        self.sound = 'ПППФФФФФФФ'
        self._animal_type = 'Жираф'
        self._biome = 'Пустыня'
        self._predator = False
        self._area = 20


class Lion(Animal):

    def __init__(self, name, volume_of_food, food, age):
        super().__init__(name, volume_of_food, food, age)
        self.sound = 'РРРРРРР'
        self._animal_type = 'Лев'
        self._biome = 'Саванна'
        self._predator = True
        self._area = 12


class Goat(Animal):

    def __init__(self, name, volume_of_food, food, age):
        super().__init__(name, volume_of_food, food, age)
        self.sound = 'МЕЕЕЕЕЕЕ'
        self._animal_type = 'Козел'
        self._biome = 'Равнина'
        self._predator = False
        self._area = 10

