from Aviary import *
import unittest


class Aviary_test(unittest.TestCase, Animal, Aviary):
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
