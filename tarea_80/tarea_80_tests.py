import unittest

from tarea_80 import verificar_y_calcular


class tarea_80_tests(unittest.TestCase):
    def test_que_sea_numero(self):
        """Testea que los valores no sean numeros"""
        valor1, valor2 = verificar_y_calcular("a")
        self.assertEqual(1, valor1)
        self.assertEqual(0, valor2)
        valor1, valor2 = verificar_y_calcular("Hola")
        self.assertEqual(1, valor1)
        self.assertEqual(0, valor2)
    def test_que_sea_de_la_longitud_adecuada(self):
        """Testea que no tengan más decimales que los debidos"""
        valor1, valor2 = verificar_y_calcular("0.000001")
        self.assertEqual(2, valor1)
        self.assertEqual(0, valor2)
        valor1, valor2 = verificar_y_calcular("9.99999999")
        self.assertEqual(2, valor1)
        self.assertEqual(0, valor2)

    def test_que_no_este_fuera_de_limite(self):
        """Testea que los valores no estén fuera de límites"""
        valor1, valor2 = verificar_y_calcular("10.0")
        self.assertEqual(3, valor1)
        self.assertEqual(0, valor2)
        valor1, valor2 = verificar_y_calcular("0.000")
        self.assertEqual(3, valor1)
        self.assertEqual(0, valor2)

    def test_comprueba_valores_normales(self):
        """Testea el valor correcto de la función"""
        valor1, valor2 = verificar_y_calcular("0.25")
        self.assertEqual("1", valor1)
        self.assertEqual("4", valor2)
        valor1, valor2 = verificar_y_calcular("0.75")
        self.assertEqual("3", valor1)
        self.assertEqual("4", valor2)
        valor1, valor2 = verificar_y_calcular("0.9999")
        self.assertEqual("9999", valor1)
        self.assertEqual("10000", valor2)
        valor1, valor2 = verificar_y_calcular("0.33")
        self.assertEqual("33", valor1)
        self.assertEqual("100", valor2)
        valor1, valor2 = verificar_y_calcular("0.5")
        self.assertEqual("1", valor1)
        self.assertEqual("2", valor2)
        valor1, valor2 = verificar_y_calcular("0.11")
        self.assertEqual("11", valor1)
        self.assertEqual("100", valor2)
        



if __name__ == '__main__':
    unittest.main()