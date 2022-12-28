from Aviary import *
from Imports import *
import unittest


class Aviary_test(unittest.TestCase):
    def setUp(self):
        self.Aviary = Aviary

    def test_no_add(self):
        Manny = Giraffe('Мэнни', 3, 20)
        W = Aviary('Травоядные', 'Пустыня', 10)
        W.add(Manny)
        expected = []
        actual = W.animals
        self.assertEqual(expected, actual)

    def test_add_predator_and_herbivore(self):
        Simba = Tiger('Симба', 5, 5)
        Petya = Elefant('Петя', 5, 20)
        V = Aviary('Tigers', 'Равнина', 100)
        V.add(Simba)
        V.add(Petya)
        expected = [Simba]
        actual = V.animals
        self.assertEqual(expected, actual)

    def test_add_herbivore_and_predator(self):
        Ksenia = Mouse('Мышь', 5, 20)
        Simba = Tiger('Симба', 5, 5)
        V = Aviary('Tigers', 'Равнина', 100)
        V.add(Ksenia)
        V.add(Simba)
        expected = [Ksenia]
        actual = V.animals
        self.assertEqual(expected, actual)

    def test_add_giraffe_in_plain(self):
        Manny = Giraffe('Мэнни', 3, 20)
        W = Aviary('Травоядные', 'Равнина', 100)
        W.add(Manny)
        expected = []
        actual = W.animals
        self.assertEqual(expected, actual)

    def test_add_herbivore_and_herbivore(self):
        Manny = Giraffe('Мэнни', 3, 20)
        Petya = Elefant('Петя', 5, 20)
        W = Aviary('Травоядные', 'Пустыня', 100)
        W.add(Manny)
        W.add(Petya)
        expected = [Manny, Petya]
        actual = W.animals
        self.assertEqual(expected, actual)

    def test_add_predator_and_predator(self):
        Simba = Tiger('Симба', 5, 5)
        Slava = Tiger('Слава', 10, 20)
        Bosia = Tiger('Бося', 10, 15)
        V = Aviary('Tigers', 'Равнина', 25)
        V.add(Simba)
        V.add(Slava)
        V.add(Bosia)
        expected = [Simba, Slava]
        actual = V.animals
        self.assertEqual(expected, actual)

    def test_delete(self):
        Simba = Tiger('Симба', 5, 5)
        Slava = Tiger('Слава', 10, 12)
        V = Aviary('Tigers', 'Равнина', 100)
        V.add(Simba)
        V.add(Slava)
        V.delete(Simba)
        expected = [Slava]
        actual = V.animals
        self.assertEqual(expected, actual)

    def test_delete_all(self):
        Simba = Tiger('Симба', 5, 5)
        Slava = Tiger('Слава', 10, 12)
        V = Aviary('Tigers', 'Равнина', 100)
        V.add(Simba)
        V.add(Slava)
        V.delete_all()
        expected = []
        actual = V.animals
        self.assertEqual(expected, actual)

    def test_feed(self):
        Simba = Tiger('Симба', 5, 5)
        V = Aviary('Tigers', 'Равнина', 100)
        V.add(Simba)
        V.feed(5, "Мясо")
        expected = 5
        actual = Simba.satiety
        self.assertEqual(expected, actual)

    def test_not_feed(self):
        Simba = Tiger('Симба', 5, 5)
        Slava = Tiger('Слава', 10, 10)
        V = Aviary('Tigers', 'Равнина', 100)
        V.add(Simba)
        V.add(Slava)
        V.feed(3, "Мясо")
        expected = 3, 3
        actual = Simba.satiety, Slava.satiety
        self.assertEqual(expected, actual)

    def test_overeated(self):
        Simba = Tiger('Симба', 5, 5)
        Slava = Tiger('Слава', 10, 10)
        V = Aviary('Tigers', 'Равнина', 100)
        V.add(Simba)
        V.add(Slava)
        V.feed(11, "Мясо")
        expected = 11, 11
        actual = Simba.satiety, Slava.satiety
        self.assertEqual(expected, actual)