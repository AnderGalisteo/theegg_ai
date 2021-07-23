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
    return



if __name__ == "__main__":
    val = input("Introduzca su valor entre 0.0001 y 0.9999: ")
    numerador, denominador = verificar_y_calcular(val)
    if not(denominador == 0):
        print(numerador+"/"+denominador)

