import unittest

from tarea_45 import findsequentialnumber,findbinarynumber

class tarea_45_tests(unittest.TestCase):
    def test_1(self):
        """Testea que los valores no sean numeros"""
        valor1 = findsequentialnumber([3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56],874)
        self.assertEqual(11, valor1)
        valor1 = findbinarynumber([3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56],874)
        self.assertEqual(3, valor1)

    



if __name__ == '__main__':
    unittest.main()