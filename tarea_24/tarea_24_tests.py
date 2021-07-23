import unittest

from tarea_24 import dec_a_binario


class tarea_24_tests(unittest.TestCase):
    def test_que_sea_numero(self):
        """Testea que los valores no sean numeros"""
        valor1 = dec_a_binario("a")
        self.assertEqual(-1, valor1)
        valor1 = dec_a_binario("Hola")
        self.assertEqual(-1, valor1)

    def test_que_no_este_fuera_de_limite(self):
        """Testea que los valores no estén fuera de límites"""
        valor1 = dec_a_binario("10.0")
        self.assertEqual(-1, valor1)
        valor1 = dec_a_binario("-0.0001")
        self.assertEqual(-1, valor1)

    def test_comprueba_valores_normales(self):
        """Testea el valor correcto de la función"""
        valor1 = dec_a_binario("0.25")
        self.assertEqual("111111", valor1)
        valor1 = dec_a_binario("0.75")
        self.assertEqual("10111111", valor1)
        valor1 = dec_a_binario("0.9999")
        self.assertEqual("11111110", valor1)
        valor1 = dec_a_binario("0.33")
        self.assertEqual("1010100", valor1)
        valor1 = dec_a_binario("0.5")
        self.assertEqual("1111111", valor1)
        valor1 = dec_a_binario("0.11")
        self.assertEqual("11100", valor1)
        valor1 = dec_a_binario("1")
        self.assertEqual("11111111", valor1)
        valor1 = dec_a_binario("0")
        self.assertEqual("0", valor1)
        



if __name__ == '__main__':
    unittest.main()