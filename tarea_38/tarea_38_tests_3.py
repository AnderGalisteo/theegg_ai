import unittest

from tarea_38_3 import encontrar_primo_palindromo


class tarea_38_tests_3(unittest.TestCase):
    def test_comprueba_valores_normales(self):
        """Testea el valor correcto de la función"""
        valor1 = encontrar_primo_palindromo(10)
        self.assertEqual(11, valor1)
        valor1 = encontrar_primo_palindromo(31)
        self.assertEqual(101, valor1)
        valor1 = encontrar_primo_palindromo(456789)
        self.assertEqual(1003001, valor1)



if __name__ == '__main__':
    unittest.main()