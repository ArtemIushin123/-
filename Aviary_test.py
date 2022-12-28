from Aviary import *
from Imports import *
import unittest


class Aviary_test(unittest.TestCase):
    def setUp(self):
        self.Aviary = Aviary

    def test_add_predator_and_herbivore(self):
        Simba = Tiger('Симба', 5, 5)
        Petya = Elefant('Петя', 5, 20)
        V = Aviary('Tigers', 'Равнина', 100)
        V.add(Simba)
        V.add(Petya)
        expected = [Simba]
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
        actual = V.feed
        self.assertEqual(expected, actual)

    def test_not_feed(self):
        Simba = Tiger('Симба', 5, 5)
        Slava = Tiger('Слава', 10, 10)
        V = Aviary('Tigers', 'Равнина', 100)
        V.add(Simba)
        V.add(Slava)
        V.feed(3, "Мясо")
        expected = 3
        actual = V.feed
        self.assertEqual(expected, actual)

    def test_overeated(self):
        Simba = Tiger('Симба', 5, 5)
        Slava = Tiger('Слава', 10, 10)
        V = Aviary('Tigers', 'Равнина', 100)
        V.add(Simba)
        V.add(Slava)
        V.feed(11, "Мясо")
        expected = 11
        actual = V.feed
        self.assertEqual(expected, actual)
