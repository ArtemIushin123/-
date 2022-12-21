from Animal import *


class Aviary_1:
    def __init__(self, name, biome, area):
        self.name = name
        self.biome = biome
        self.area = area
        self.animals = []
        self.predator = bool
        self.predator_type = ''

    def add(self, Animal: Animal):
        if len(self.animals) == 0 and Animal.predator:
            self.predator = True
            self.predator_type = Animal.animal_type
            print(Animal.animal_type, Animal.name, 'подселился в вольер', self.name)
        if Animal.predator == self.predator and Animal.biome == self.biome:
            if Animal.predator and Animal.animal_type == self.predator_type:
                self.animals.append(Animal)
            elif Animal.predator:
                print('Нельзя подселить', Animal.animal_type, Animal.name, 'в вольер', self.name)
            else:
                self.animals.append(Animal)
        else:
            print('Нельзя подселить', Animal.animal_type, Animal.name, 'в вольер', self.name)


class Aviary_2:
    def __init__(self, name, biome, area):
        self.name = name
        self.biome = biome
        self.area = area
        self.animals = []
        self.predator = bool
        self.predator_type = ''

    def add(self, Animal: Animal):
        if len(self.animals) == 0 and Animal.predator == False:
            self.predator = False
            self.predator_type = Animal.animal_type
            print(Animal.animal_type, Animal.name, 'подселился в вольер', self.name)
        if Animal.predator == self.predator and Animal.biome == self.biome:
            self.animals.append(Animal)
            if Animal.predator:
                print('Нельзя подселить', Animal.animal_type, Animal.name, 'в вольер', self.name)
            else:
                self.animals.append(Animal)
        else:
            print('Нельзя подселить', Animal.animal_type, Animal.name, 'в вольер', self.name)
