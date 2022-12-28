class Aviary:
    def __init__(self, name, biome, area):
        self.name = name
        self.biome = biome
        self.area = area
        self.animals = []
        self._free_area = area
        self.predator_type = ''
        self.predator = bool

    def add(self, Animal):
        if len(self.animals) == 0:
            self.animals.append(Animal)
            self._free_area -= Animal.area
            print(Animal.animal_type, Animal.name, 'подселился в вольер', self.name)
        elif len(self.animals) != 0 and Animal.area <= self._free_area and Animal.predator == False:
            if self.biome == Animal.biome:
                self.animals.append(Animal)
                self._free_area -= Animal.area
                print(Animal.animal_type, Animal.name, 'подселился в вольер', self.name)
            else:
                print('Нельзя подселить', Animal.animal_type, Animal.name, 'в вольер', self.name)
        elif len(self.animals) != 0 and Animal.area <= self._free_area and Animal.predator == True:
            if self.predator_type != Animal.animal_type and self.biome == Animal.biome:
                self.animals.append(Animal)
                self._free_area -= Animal.area
                print(Animal.animal_type, Animal.name, 'подселился в вольер', self.name)
            else:
                print('Нельзя подселить', Animal.animal_type, Animal.name, 'в вольер', self.name)
        else:
            print('Нельзя подселить', Animal.animal_type, Animal.name, 'в вольер', self.name)

    def feed(self, value, food):
        for i in self.animals:
            i.eat(value, food)

    def delete(self, name):
        self.animals.remove(name)
        print(name.animal_type, name.name, 'удален из', self.name)

    def sound_animal(self):
        for i in self.animals:
            i.sound_animal()

    def delete_all(self):
        self.animals.clear()
        print('Все животные из вольера', self.name, 'были выселены из-за неуплаты квартплаты')

    @property
    def free_size(self):
        return self._free_area
