import unittest

from tarea_38_1 import encontrar_conjunto_largo


class tarea_38_tests_1(unittest.TestCase):
    def test_comprueba_valores_normales(self):
        """Testea el valor correcto de la función"""
        valor1 = encontrar_conjunto_largo("ctgactga", "actgagc")
        self.assertEqual("actga", valor1)
        valor1 = encontrar_conjunto_largo("cgtaattgcgat", "cgtacagtagc")
        self.assertEqual("cgta", valor1)
        valor1 = encontrar_conjunto_largo("ctgggccttgaggaaaactg", "gtaccagtactgatagt")
        self.assertEqual("actg", valor1)
        



if __name__ == '__main__':
    unittest.main()