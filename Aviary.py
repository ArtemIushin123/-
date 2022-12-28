class Aviary:
    def __init__(self, name, biome, area):
        self.name = name
        self.biome = biome
        self.area = area
        self.animals = []
        self._free_area = area
        self.predator_type = ''
        self.predator = bool

    def add(self, animal):
        if len(self.animals) == 0 and animal.area <= self._free_area and self.biome == animal.biome:
            self.animals.append(animal)
            self._free_area -= animal.area
            print(animal.animal_type, animal.name, 'подселился в вольер', self.name)
        elif len(self.animals) != 0 and animal.area <= self._free_area and animal.predator == False:
            if self.biome == animal.biome:
                self.animals.append(animal)
                self._free_area -= animal.area
                print(animal.animal_type, animal.name, 'подселился в вольер', self.name)
            else:
                print('Нельзя подселить', animal.animal_type, animal.name, 'в вольер', self.name)
        elif len(self.animals) != 0 and animal.area <= self._free_area and animal.predator == True:
            if self.predator_type == animal.animal_type and self.biome == animal.biome:
                self.animals.append(animal)
                self._free_area -= animal.area
                print(animal.animal_type, animal.name, 'подселился в вольер', self.name)
            else:
                print('Нельзя подселить', animal.animal_type, animal.name, 'в вольер', self.name)
        else:
            print('Нельзя подселить', animal.animal_type, animal.name, 'в вольер', self.name)

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
