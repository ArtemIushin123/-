from Animal import *
from Aviary import *
Petya = Elefant('Петя', 5, 'сена', 20)
Simba = Tiger('Симба', 5, 'мяса', 5)
Matilda = Pinguin('Матильда', 0.3, 'рыбы', 1)
Zlata = Dog('Злата', 1, 'корм', 2)
Suzi = Sheep('Сьюзи', 2, 'сена', 5)
Vladislav = Wolf('Владислав', 5, 'мяса', 12)
Manny = Giraffe('Мэнни', 3, 'сена', 20)
Miron = Lion('Мирон', 10, 'мяса', 7)
Danya = Goat('Даня', 7, 'сена', 16)

Petya.eat()
Petya.sound_animal()
Petya.play()

Simba.eat()
Simba.sound_animal()
Simba.play()

Matilda.eat()
Matilda.sound_animal()
Matilda.play()

Zlata.eat()
Zlata.sound_animal()
Zlata.play()

Suzi.eat()
Suzi.sound_animal()
Suzi.play()

Vladislav.eat()
Vladislav.sound_animal()
Vladislav.play()

Manny.eat()
Manny.sound_animal()
Manny.play()

Miron.eat()
Miron.sound_animal()
Miron.play()

Danya.eat()
Danya.sound_animal()
Danya.play()

V = Aviary_1('Tigers', 'Равнина', 100)
V.add(Tiger('Симба', 5, 'мяса', 5))
V.add(Giraffe('Мэнни', 3, 'сена', 20))

V = Aviary_2('Травоядные пустынные', 'Пустыня', 100)
V.add(Elefant('Петя', 5, 'сена', 20))
V.add(Sheep('Сьюзи', 2, 'сена', 5))
