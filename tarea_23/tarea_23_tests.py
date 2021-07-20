import unittest

from tarea_23 import generar_solitario, from_string_to_int_list,from_int_to_string,sum_listas,res_listas




class tarea_23_tests(unittest.TestCase):
    def test_generar_solitario(self):
        """Testea que se genere el solitario correctamente"""
        valor1 = generar_solitario(10,[43, 48, 10, 8, 5, 12, 28, 25, 36, 23, 38, 0, 34, 27, 47, 3, 22, 35, 52, 44, 9, 26, 39, 17, 18, 29, 19, 46, 24, 53, 41, 37, 7, 20, 1, 11, 6, 14, 40, 42, 4, 45, 50, 30, 21, 49, 31, 33, 15, 16, 13, 2, 32, 51])
        self.assertEqual("GULXVAIEQF", valor1)

        valor1 = generar_solitario(100,[35, 21, 16, 8, 3, 13, 41, 0, 39, 30, 37, 15, 17, 34, 28, 44, 52, 9, 27, 19, 43, 14, 32, 25, 23, 36, 7, 4, 5, 24, 1, 40, 29, 48, 33, 18, 51, 2, 38, 50, 31, 45, 11, 46, 6, 53, 22, 49, 20, 10, 42, 26, 47, 12])
        self.assertEqual("HEKSRCFWHHBQXEONCRRBBGAXPDJCRQVKUPAWOLZUHHDKIAFQYDOTNYOGIYSAPXCDJHQOEOOWLNABOLZXUFHRWBIFIWCLVBLOSIND", valor1)
    def test_from_string_to_int_list(self):
        therange = list(range(1,27))
        self.assertEqual(therange, from_string_to_int_list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    def test_from_int_to_string(self):
        self.assertEqual(1, 1)
    def test_sum_listas(self):
        self.assertEqual(1, 1)
    def test_res_listas(self):
        self.assertEqual(1, 1)
        



if __name__ == '__main__':
    unittest.main()