from classs import *
from aviary import *
Petya = Elefant('Петя', '5 кг сена', '20 лет')
Simba = Tiger('Симба', '5 кг мяса или рыбы', '5 лет')
Matilda = Pinguin('Матильда', '0.3 рыбы',  '1 год')

Petya.eat()
Petya.sound_animal()
Petya.play()
Simba.eat()
Simba.sound_animal()
Simba.play()
Matilda.eat()
Matilda.sound_animal()
Matilda.play()

V = Aviary('Elefant', "5 кг сена", "Пустыня")
V.add(Pinguin('Матильда', '0.3 рыбы',  '1 год'))