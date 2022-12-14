from Imports import *
from Aviary import *

Petya = Elefant('Петя', 5, 20)
Ksenia = Mouse('Ксения', 1, 2)
Simba = Tiger('Симба', 5, 5)
Slava = Tiger('Слава', 10, 20)
Bosia = Tiger('Бося', 10, 15)
Matilda = Pinguin('Матильда', 0.3, 1)
Manny = Giraffe('Мэнни', 3, 20)
Vladik = Wolf('Владик', 3, 6)
Petya.eat(food='Бананы', value=4)
Petya.sound_animal()
Petya.play()
print('')
Ksenia.eat(food='Зерно', value=5)
Ksenia.sound_animal()
Ksenia.play()
print('')
Simba.eat(food='Мясо', value=5)
Simba.sound_animal()
Simba.play()
print('')
Slava.eat(food='Мясо', value=8)
Slava.sound_animal()
Slava.play()
print('')
Matilda.eat(food='Лук', value=3)
Matilda.sound_animal()
Matilda.play()
print('')
Manny.eat(food='Человек', value=1000)
Manny.sound_animal()
Manny.play()
print('')
Vladik.eat(food='Мясо', value=1)
Vladik.sound_animal()
Vladik.play()
print('')
V = Aviary('Хищники', 'Равнина', 100)
V.add(Simba)
V.add(Slava)
V.add(Vladik)
V.add(Bosia)
V.sound_animal()
V.feed(food='Мясо', value=6)
V.delete_all()
print('')
W = Aviary('Травоядные', 'Пустыня', 100)
W.add(Manny)
W.add(Petya)
W.add(Matilda)
W.sound_animal()
W.feed(food='Бананы', value=6)
W.delete_all()
print('')
B = Aviary('Хищники', 'Тундра', 100)
B.add(Matilda)
B.add(Ksenia)
B.add(Slava)
B.sound_animal()
B.feed(food='Рыба', value=6)
B.delete(Matilda)
B.delete_all()
