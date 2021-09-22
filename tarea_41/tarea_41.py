"""
Para esta tarea proponemos el siguiente ejercicio: el @egger mediante técnicas de Regex debe 
calcular el número de caracteres, el número palabras y ranking de palabras por frecuencia de uso
del siguiente texto. La aplicación debe servir para cualquier otro texto:

"En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como 
referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento?
Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas 
olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por 
hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo, 
ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.
Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta 
increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando 
quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no 
porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alemán me 
solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso 
yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.
El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios 
congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando 
semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno.
Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar 
hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que 
se encarga de pensar, y hasta cantamos juntos la canción de Annie.
Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de 
Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así."
"""
"""
Se nos dice que es un valor decimal pero no en que rango. Yo voy a coger un valor entre 0 y 1. 1 se mapeara a "11111111" equivalente a 255 y 0 a 0. 
Cualquier valor intermedio será interpretado proporcionalmente. Si el valor está fuera de rango, devolverá -1, un error.
Los "leading zeros" he decidido quitarlos, ya que así la solución es mś limpia en caso de números pequeños.
"""
import re
import operator

def get_count_char(text):
    sentence = text
    allchar = re.findall('[0-9a-zA-Z ,.«»á-ú]', sentence)
    return len(allchar)
def get_count_words(text):
    sentence = text
    allchar = re.findall('\\w+', sentence)
    return len(allchar)
def get_frequency(text):
    frecuencia_palabras = {}
    sentence = text
    allwords = re.findall('\\w+', sentence)
    for palabra in allwords:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1

    # Ordenar las palabras en función de la frecuencia de aparición
    ranking_palabras = sorted(frecuencia_palabras.items(), key=operator.itemgetter(1), reverse=True)
    return [i[0] for i in ranking_palabras]

if __name__ == "__main__":
    text = "En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento? Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo, ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo. Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alemán me solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda. El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno. Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que se encarga de pensar, y hasta cantamos juntos la canción de Annie. Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así."
    print(get_count_char(text))
    print(get_count_words(text))
    print(get_frequency(text))