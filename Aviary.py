from Animal import *


class Aviary:
    def __init__(self, name, biome, area):
        self.name = name
        self.biome = biome
        self.area = area
        self.animals = []
        self.predator = False
        self.predator_type = ''

    def add(self, Animal: Animal):
        if Animal.predator_or_herbivore and len(self.animals) == 0:
            self.predator = True
            self.predator_type = Animal._animal_type
        if Animal.predator_or_herbivore == self.predator and Animal.biome == self.biome:
            if Animal.predator_or_herbivore and Animal.view == self.predator_type:
                self.animals.append(Animal)
            elif Animal.predator_or_herbivore:
                print('Нельзя подселить', Animal._animal_type)
            else:
                self.animals.append(Animal)
        else:
            print('Нельзя подселить', Animal._animal_type)
