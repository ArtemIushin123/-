from Animal import *
from Aviary import *
Petya = Elefant('Петя', '5 кг сена', 20)
Simba = Tiger('Симба', '5 мяса или рыбы', 5)
Matilda = Pinguin('Матильда', '0.3 кг рыбы',  1)
Zlata = Dog('Злата', '1 кг корма', 2)
Suzi = Sheep('Сьюзи', '2 кг сена', 5)
Vladislav = Wolf('Владислав', '5 кг мяса', 12)
Manny = Giraffe('Мэнни', '3 кг сена', 20)
Miron = Lion('Мирон', '10 кг мяса', 7)
Danya = Goat('Даня', '7 кг сена', 16)

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

V = Aviary('Elefant', 5, "Пустыня")
V.add(Pinguin('Матильда', '0.3', 1))
V.add(Giraffe('Мэнни', '3', 20))
