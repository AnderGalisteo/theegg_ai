import unittest

from tarea_38_2 import invertir


class tarea_38_tests_1(unittest.TestCase):
    def test_comprueba_valores_normales(self):
        """Testea el valor correcto de la función"""
        valor1 = invertir(["this is a test","foobar","all your base"])
        self.assertEqual(["Case #1: test a is this","Case #2: foobar","Case #3: base your all"], valor1)



if __name__ == '__main__':
    unittest.main()