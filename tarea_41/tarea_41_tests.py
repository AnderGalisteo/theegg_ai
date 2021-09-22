import unittest

from tarea_41 import get_count_char,get_count_words,get_frequency

text = "En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento? Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo, ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo. Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alemán me solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda. El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno. Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que se encarga de pensar, y hasta cantamos juntos la canción de Annie. Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así."


class tarea_24_tests(unittest.TestCase):
    def alltests(self):
        """Testea que los valores no sean numeros"""
        valor1 = get_count_char(text)
        self.assertEqual(1879, valor1)
        valor1 = get_count_words(text)
        self.assertEqual(348, valor1)
        valor1 = get_frequency(text)
        self.assertEqual(['de', 'y', 'en', 'la', 'un', 'que', 'el', 'se', 'los', 'me', 'una', 'a', 'Irlanda', 'Chris', 'está', 'Y', 'por', 'no', 'neopreno', 'para', 'Strandhill', 'mi', 'señor', 'es', 'playa', 'muy', 'allí', 'yo', 'también', 'unos', 'costa', 'las', 'Aunque', 'tenía', 'ni', 'tabla', 'había', 'lo', 'del', 'Me', 'uno', 'su', 'agua', 'con', 'cabeza', 'paseo', 'hasta', 'Annie', 'En', 'cruzó', 'camino', 'inspiran', 'posicionan', 'como', 'referente', 'Fue', 'pieza', 'fundamental', 'momento', 'pura', 'congelación', 'Te', 'cuento', 'donde', 'mar', 'ruge', 'bien', 'siempre', 'lleno', 'surfistas', 'busca', 'buenas', 'olas', 'estaba', 'Después', 'meses', 'viviendo', 'ciudad', 'sin', 'mis', 'ganas', 'hacer', 'poco', 'surfing', 'estaban', 'nubes', 'pequeño', 'problema', 'equipo', 'tampoco', 'ninguna', 'tienda', 'alquilarlo', 'Todo', 'puso', 'rodar', 'enseguida', 'Escribí', 'famoso', 'surfista', 'zona', 'recibí', 'respuesta', 'increíble', 'Mi', 'casa', 'calle', 'x', 'puerta', 'abierta', 'tienes', 'esquina', 'Ven', 'cuando', 'quieras', 'dijo', 'eso', 'hice', 'fui', 'allá', 'cogí', 'pudo', 'prestar', 'porque', 'negara', 'Lamentablemente', 'le', 'sacaba', '15', 'cm', 'altura', 'Luego', 'alemán', 'solucionó', 'tema', 'prestó', 'maletero', 'fino', 'uso', 'Mediterráneo', 'otoño', 'o', 'primavera', 'claro', 'era', 'invierno', 'estábamos', 'El', 'caso', 'salí', 'más', 'pronto', 'previsto', 'manos', 'labios', 'congelados', 'empecé', 'cambiar', 'mismo', 'contorneaba', 'estando', 'semidesnudo', 'acercó', 'Está', 'fría', 'eh', 'apuntó', 'este', 'fenómeno', 'superaba', '65', 'años', 'todos', 'días', 'hacía', 'recorrido', 'decenas', 'kilómetros', 'llegar', 'Sus', 'gracietas', 'buena', 'conversación', 'hicieron', 'apartar', 'frío', 'parte', 'encarga', 'pensar', 'cantamos', 'juntos', 'canción', 'Sé', 'esto', 'último', 'puede', 'sonar', 'raro', 'quién', 'canta', 'semidesudo', 'congelado', 'acaba', 'conocer', 'Pero', 'seguro', 'ti', 'te', 'han', 'pasado', 'cosas', 'así'], valor1)


    



if __name__ == '__main__':
    unittest.main()