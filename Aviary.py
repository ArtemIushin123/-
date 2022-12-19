from Animal import *


class Aviary:
    def __init__(self, name, biome, square):
        self.name = name
        self.biome = biome
        self.square = square
        self.animals = []
        self.predator = False
        self.predator_type = ''

    def add(self, Animal: Animal):
        if Animal.predator == True and len(self.animals) == 0:
            self.predator = True
            self.predator_type = Animal.view
        if Animal.predator == self.predator and Animal.biome == self.biome:
            if Animal.predator == True and Animal.view == self.predator_type:
                self.animals.append(Animal)
            elif Animal.predator == True:
                print('Нельзя подселить', Animal.view)
            else:
                self.animals.append(Animal)
        else:
            print('Нельзя подселить', Animal.view)
