class Animal:

    ANIMAL_PREDATOR = 'Хищник'
    ANIMAL_HERBIVORE = 'Травоядное'

    def __init__(self, name, volume_of_food, age):
        self.name = name
        self._volume_of_food = volume_of_food
        self.age = age
        self.sound = ''
        self._animal_type = ''
        self._biome = ''
        self._area = ''
        self._predator_or_herbivore = bool

    def play(self):
        print(self.name, ': Я поиграл')

    def sound_animal(self):
        print(self.name, ':', self.sound)

    def eat(self):
        print(self.name, ':', 'Я ем', self.volume_of_food)

    @property
    def volume_of_food(self):
        return self._volume_of_food

    @property
    def view(self):
        return self._animal_type

    @property
    def biome(self):
        return self._biome

    @property
    def square(self):
        return self._area

    @property
    def predator_or_herbivore(self):
        return self._predator_or_herbivore

    @property
    def animal_type(self):
        return self._animal_type


class Elefant(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'УУХХЕРРРРРРРРРРРРРРРРРР'
        self._animal_type = 'Слон'
        self._biome = 'Пустыня'
        self.ANIMAL_HERBIVORE = 'Травоядное'
        self._square = '15 м**2'


class Tiger(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'РРРРРР'
        self._animal_type = 'Тигр'
        self._biome = 'Тропики'
        self.ANIMAL_PREDATOR = 'Хищник'
        self._square = '10 м**2'


class Pinguin(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'Хрю'
        self._animal_type = 'Пингвин'
        self._biome = 'Тундра'
        self.ANIMAL_PREDATOR = 'Хищник'
        self._square = '5 м**2'


class Dog(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'Гав'
        self._animal_type = 'Собака'
        self._biome = 'Тундра'
        self.ANIMAL_PREDATOR = 'Хищник'
        self._square = '3 м**2'


class Sheep(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'БЕЕЕЕ'
        self._animal_type = 'Овца'
        self._biome = 'Горы'
        self.ANIMAL_HERBIVORE = 'Травоядное'
        self._square = '8 м**2'


class Wolf(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'РРРРРР'
        self._animal_type = 'Волк'
        self._biome = 'Равнина'
        self.ANIMAL_PREDATOR = 'Хищник'
        self._square = '3 м**2'


class Giraffe(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'Слова жирафа'
        self._animal_type = 'Жираф'
        self._biome = 'Пустыня'
        self.ANIMAL_HERBIVORE = 'Травоядное'
        self._square = '20 м**2'


class Lion(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'РРРРРРР'
        self._animal_type = 'Лев'
        self._biome = 'Саванна'
        self.ANIMAL_PREDATOR = 'Хищник'
        self._square = '12 м**2'


class Goat(Animal):

    def __init__(self, name, volume_of_food, age):
        super().__init__(name, volume_of_food, age)
        self.sound = 'МЕЕЕЕЕЕЕ'
        self._animal_type = 'Козел'
        self._biome = 'Равнина'
        self.ANIMAL_HERBIVORE = 'Травоядное'
        self._square = '10 м**2'



