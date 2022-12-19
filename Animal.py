class Animal:

    def __init__(self, name, volume_of_food, age):
        self.name = name
        self._volume_of_food = volume_of_food
        self.age = age
        self.sound = ''
        self._view = ''
        self._biome = ''
        self._square = ''
        self._predator = bool

    def play(self):
        print(self.name, ': Я поиграл')

    def sound_animal(self):
        print(self.name, ':', self.sound)

    def eat(self):
        print(self.name, 'Я ем', self.volume_of_food)

    @property
    def volume_of_food(self):
        return self._volume_of_food

    @property
    def view(self):
        return self._view

    @property
    def biome(self):
        return self._biome

    @property
    def square(self):
        return self._square

    @property
    def predator(self):
        return self._predator


class Elefant(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'УУХХЕРРРРРРРРРРРРРРРРРР'
        self._view = 'Слон'
        self._biome = 'Пустыня'
        self._predator = 'Травоядное'
        self._square = '15 м**2'


class Tiger(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'РРРРРР'
        self._view = 'Тигр'
        self._biome = 'Тропики'
        self._predator = 'Хищник'
        self._square = '10 м**2'


class Pinguin(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'Хрю'
        self._view = 'Пингвин'
        self._biome = 'Тундра'
        self._predator = 'Хищник'
        self._square = '5 м**2'


class Dog(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'Гав'
        self._view = 'Собака'
        self._biome = 'Тундра'
        self._predator = 'Хищник'
        self._square = '3 м**2'


class Sheep(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'БЕЕЕЕ'
        self._view = 'Овца'
        self._biome = 'Горы'
        self._predator = 'Травядное'
        self._square = '8 м**2'


class Wolf(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'РРРРРР'
        self._view = 'Волк'
        self._biome = 'Равнина'
        self._predator = 'Хищник'
        self._square = '3 м**2'


class Giraffe(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'Слова жирафа'
        self._view = 'Жираф'
        self._biome = 'Пустыня'
        self._predator = 'Травоядное'
        self._square = '20 м**2'


class Lion(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'РРРРРРР'
        self._view = 'Лев'
        self._biome = 'Саванна'
        self._predator = 'Хищник'
        self._square = '12 м**2'


class Goat(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'МЕЕЕЕЕЕЕ'
        self._view = 'Козел'
        self._biome = 'Равнина'
        self._predator = 'Травоядное'
        self._square = '10 м**2'



