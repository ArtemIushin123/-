from Aviary import *
import unittest


class Aviary_test(unittest.TestCase):
    def setUp(self):
        self.Aviary = Aviary

    def test_add(self):
        Simba = Tiger('Симба', 5, 'мяса', 5)
        Petya = Elefant('Петя', 5, 'сена', 20)
        V = Aviary('Tigers', 'Равнина', 100)
        V.add(Simba)
        V.add(Petya)
        expected = [Simba]
        actual = V.animals
        self.assertEqual(expected, actual)
