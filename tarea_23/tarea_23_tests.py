import unittest
import random

from tarea_23 import generar_solitario, from_string_to_int_list,from_int_to_string,sum_listas,res_listas,cifrar,descifrar




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
        therange = list(range(1,27))
        self.assertEqual("ABCDEFGHIJKLMNOPQRSTUVWXYZ", from_int_to_string(therange))
    def test_sum_listas(self):
        therange = list(range(1,27))
        therange_reversed = therange.copy()
        therange_reversed.reverse()
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], sum_listas(therange,therange_reversed))

        self.assertEqual([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25], sum_listas(therange,therange))
    def test_res_listas(self):
        therange = list(range(1,27))
        therange_reversed = therange.copy()
        therange_reversed.reverse()
        #self.assertEqual([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25], res_listas(therange,therange_reversed))
        self.assertEqual([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25], res_listas(therange,therange_reversed))

        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], res_listas(therange,therange))
    def test_functional(self):
        texto="En un lugar de la Mancha de cuyo nombre no quiero acordarme no ha mucho tiempo que vivia un hidalgo de los de lanza en astillero adarga antigua rocin flaco y galgo corredor Una olla de algo mas vaca que carnero salpicon las mas noches duelos y quebrantos los sabados lantejas los viernes algun palomino de anadidura los domingos consumian las tres cuartas partes de su hacienda El resto della concluian sayo de velarte calzas de velludo para las fiestas con sus pantuflos de lo mesmo y los dias de entresemana se honraba con su vellori de lo mas fino Tenia en su casa una ama que pasaba de los cuarenta y una sobrina que no llegaba a los veinte y un mozo de campo y plaza que asi ensillaba el rocin como tomaba la podadera Frisaba la edad de nuestro hidalgo con los cincuenta anos era de complexion recia seco de carnes enjuto de rostro gran madrugador y amigo de la caza Quieren decir que tenia el sobrenombre de Quijada o Quesada que en esto hay alguna diferencia en los autores que deste caso escriben aunque por conjeturas verosimiles se deja entender que se llamaba Quejana Pero esto importa poco a nuestro cuento basta que en la narracion del no se salga un punto de la verdad"
        baraja = list(range(0,54))
        random.shuffle(baraja)
        baraja1 = baraja.copy()
        
        
        textotras=descifrar(cifrar(texto,baraja1),baraja)
        self.assertEqual(texto.upper().replace(" ", ""),textotras)

if __name__ == '__main__':
    unittest.main()