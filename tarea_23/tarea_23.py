"""
Cifrar con Solitario

Solitario es un cifrado "stream", en modo "output-feedback" (salida- retroalimentación). Algunas veces se les llama generadores de claves ("Key-Generator", KG en la jerga militar de EE.UU.). La idea básica es que Solitario genera una ristra de números, llamada "keystream" (ristra o secuencia de clave), entre 1 y 26. Para cifrar, se genera una ristra de longitud igual al texto original. Seguidamente se suman, módulo 26, letra a letra al texto original, para crear el texto cifrado. Para descifrar, se genera la misma ristra y se resta, módulo 26, del texto cifrado. No te preocupes, explicaré qué es "módulo" en un minuto.

Por ejemplo, para cifrar el primer mensaje mencionado en la novela de Stephenson, "DO NOT USE PC":

    Divide el mensaje original en grupos de cinco letras (No hay nada mágico respecto a los grupos de cinco letras, es sólo tradición). Usa "X" para completar el último grupo. Así, si el mensaje es "DO NOT USE PC", el texto se transformará en:

         DONOT USEPC

    Usa Solitario para generar una ristra de letras (los detalles se dan más tarde). Supongamos que son:

         KDWUP ONOWT

    Convertimos el mensaje original de letras a números, A=1, B=2, etc:

         4 15 14 15 20   21 19 5 16 3

    Convertimos la ristra de Solitario de forma similar:

         11 4 23 21 16   15 14 15 23 20

    Sumamos los números de mensaje original con los correspondientes de la ristra Solitario, módulo 26. Es decir, si suman más de 26, restamos 26 de resultado. Por ejemplo, 1+1=2, 26+1=27, y 27-26=1, así que 26+1=1.

         15 19 11 10 10   10 7 20 13 23 

    Convertimos los números de nuevo a letras:

         OSKJJ JGTMW

Si eres realmente bueno, puedes aprender a sumar letras en tu cabeza, y simplemente sumar las letras del paso (1) y (2). Sólo hace falta un poco de práctica. Es fácil recordar que A+A=B; recordar que T+Q=K es más difícil. 
"""
def generar_solitario(tamano):
    return "A"*tamano
def divide_into_chunks(frase, tamano):
    chunks, chunk_size = len(frase), tamano
    splitted_frase = [ frase[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
    return splitted_frase
def from_string_to_int_list(frase):
    return [int(i)-64 for i in list(map(str, map(ord, list(frase))))]

def cifrar(frase):
    frase = frase.upper().replace(" ", "")
    if not(len(frase)%5 == 0):
        frase = frase + "X"*(5-len(frase)%5)
    #splitted_frase = divide_into_chunks(frase, 5)
    solitario = generar_solitario(len(frase))
    #splitted_solitario = divide_into_chunks(solitario, 5)
    test_list = from_string_to_int_list(frase)
    print(test_list)




if __name__ == "__main__":
    frase = input("Introduzca la frase: ")
    
    cifrar(frase)

