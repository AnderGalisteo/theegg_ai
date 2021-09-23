"""
Tenemos la siguiente lista de elementos: [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56].
1.- Construye tu propio algoritmo para ordenarlo de menor a mayor.
2.-
Busca el número 874 utilizando el algoritmo secuencial y el binario. En cada iteración se debe sumar +1 
de modo que al final del programa se debe indicar el número de iteraciones realizadas por cada 
algoritmo hasta encontrar el elemento.
3.- Realiza el análisis en Notación Big O (visto en la tarea #44) y describe tu conclusiones en un 
documento de texto."
"""
"""
Ejercicio muy sencillo. Implemento el bubble sort y también el sort por defecto de las listas de python.
Para encontrarlo secuencialmente, hago un loop por la lista hasta encontrarlo, sumando 1 en cada elemento.
Para el binario, utilizo 3 puntero, inicio, final y centro de la lista. Voy actualizando sus valores hasta dar con el elemento. So no lo encuentro, devuelvo -1
"""

def bubbleSort( theSeq ):
    n = len( theSeq )

    for i in range( n - 1 ) :
        flag = 0

        for j in range(n - 1) :
            
            if theSeq[j] > theSeq[j + 1] : 
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                flag = 1

        if flag == 0:
            break

    return theSeq

def sorting_alg(alist):
    alist.sort()
    return alist

def findsequentialnumber(alist,number):
    ordered_list = bubbleSort(alist)
    iterations = 0
    for i in ordered_list:
        iterations += 1
        if i == number:
            return iterations
    return -1

def findbinarynumber(alist,number):
    ordered_list = bubbleSort(alist)
    iterations = 0
    pos_init = 0
    pos_final = len(ordered_list)
    pos_half = int((pos_final+pos_init)/2)
    pos_previo = pos_half
    while 1:
        iterations += 1
        if ordered_list[pos_half] == number:
            return iterations
        if ordered_list[pos_half] > number:
            pos_final = pos_half
        else:
            pos_init = pos_half
        pos_half = int((pos_final+pos_init)/2)
        if pos_previo == pos_half:
            return -1
        else:
            pos_previo = pos_half



if __name__ == "__main__":
    print(findsequentialnumber([3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56],874))
    print(findbinarynumber([3, 56, 21, 33, 874,  123, 66, 1000, 23, 45, 65, 56],874))
