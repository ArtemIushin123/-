from Animal import *
from Aviary import *
Petya = Elefant('Петя', 5, 'сена', 20)
Simba = Tiger('Симба', 5, 'мяса', 5)
Matilda = Pinguin('Матильда', 0.3, 'рыбы', 1)
Zlata = Dog('Злата', 1, 'корм', 2)
Vladislav = Wolf('Владислав', 5, 'мяса', 12)
Manny = Giraffe('Мэнни', 3, 'сена', 20)
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

Vladislav.eat()
Vladislav.sound_animal()
Vladislav.play()

Manny.eat()
Manny.sound_animal()
Manny.play()


Danya.eat()
Danya.sound_animal()
Danya.play()

V = Aviary('Tigers', 'Равнина', 100)
V.add(Simba)
V.add(Danya)
