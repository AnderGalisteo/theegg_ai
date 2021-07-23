"""
Eres un biólogo que examina secuencias de ADN de formas de vida diferentes. Se te darán dos secuencias de ADN, y el objetivo es encontrar el conjunto ordenado de bases adyacentes de mayor tamaño que es común en ambos ADNs.

Las secuencias de ADN se darán como conjuntos ordenados de bases de nucleótidos: adenina (abreviado A), citosina (C), guanina (G) y timina (T):

ATGTCTTCCTCGA TGCTTCCTATGAC

Para el ejemplo anterior, el resultado es CTTCCT porque que es el conjunto ordenado de bases adyacentes de mayor tamaño que se encuentra en ambas formas de vida.



Ejemplo de entrada



ctgactga actgagc

cgtaattgcgat cgtacagtagc

ctgggccttgaggaaaactg gtaccagtactgatagt


Salida de la muestra



actga

cgta

actg


"""
"""
Lo he programado en python y el algoritmo es muy sencillo. Intenta dividir por 2 y luego por 3 etc hasta que encuentre un número por 
el que dividirlo o llegue hasta el mínimo entre el numerador y el denominador.
"""
def encontrar_conjunto_largo(base1, base2):

    if len(base1) >= len(base2):
        largo = base1
        corto = base2
    else:
        largo = base2
        corto = base1

    thelen = len(corto)
    for i in list(range(thelen,0,-1)):
        for j in range(0,thelen-i+1):
            if corto[0+j:i+j] in largo:
                return corto[0+j:i+1+j]

    return ""



if __name__ == "__main__":
    base1 = input("Introduzca primera secuencia: ")
    base2 = input("Introduzca segunda secuencia: ")
    subconjunto = encontrar_conjunto_largo(base1, base2)
    print(subconjunto)


