"""
Dada una serie de palabras separadas por espacios, escribir la frase formada por las mismas palabras en orden inverso. Cada palabra estará formada exclusivamente por letras, y existirá exactamente un espacio entre cada pareja de palabras. La salida debe ser "Case #" seguido del número de caso, de un símbolo de "dos puntos", de un espacio en blanco y de la frase invertida.


"""
"""
Recogo el input y lo meto en una lista. Por cada elemento de la lista, split por espacio invertir y juntar.
"""
def invertir(thestrings):
    toreturn = []
    number = 1
    for i in thestrings:
        thesplitted = i.split(" ")
        thesplitted.reverse()
        reversed = " ".join(thesplitted)
        toreturn.append("Case #"+str(number)+": "+reversed)
        number = number +1
    return toreturn



if __name__ == "__main__":
    numfrases = input("Introduzca el conjuntoel número de frases: ")
    frases = []
    for i in range(int(numfrases)):
        frases.append(input(""))
    invertido = invertir(frases)
    for i in invertido:
        print(i)


