class Aviary:
    def __init__(self, name, biome, area):
        self.name = name
        self.biome = biome
        self.area = area
        self.animals = []
        self._free_area = area

    def add(self, animal):
        if self.biome != animal.biome:
            print('Нельзя подселить', animal.animal_type, animal.name, 'в вольер', self.name, '- не совпадает биом.')
        elif animal.area > self._free_area:
            print('Нельзя подселить', animal.animal_type, animal.name, 'в вольер', self.name, '- нет места.')
        else:
            has_predators_in_aviary = any(x.predator for x in self.animals)
            if len(self.animals) == 0 or \
                    not has_predators_in_aviary and not animal.predator or \
                    has_predators_in_aviary and animal.predator:
                self.animals.append(animal)
                self._free_area -= animal.area
                print(animal.animal_type, animal.name, 'подселился в вольер', self.name)

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
