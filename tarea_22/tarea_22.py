"""1.- Para este propósito tienes que definir las siguientes entradas:
Entrada: Número total de vacas en la zona de Tolosa que están a la venta.
Entrada: Peso total que el camión puede llevar.
Entrada: Lista de pesos de las vacas.
Entrada: Lista de la producción de leche por vaca, en litros por día.
2.- El algoritmo que programes tiene que calcular la siguiente salida:
Salida: Cantidad máxima de producción de leche se puede obtener."""

"""
La solución propuesta es una de fuerza bruta. Este tipo de problemas conocidos como handbag problems https://brilliant.org/wiki/backpack-problem/ son problemas 
cuya solución óptima sólo se obtiene por fuerza bruta. Normalmente se utilizan métricas subóptimas para trabajar en ello.
Aquí se pruebas todas las combinaciones.
"""

import itertools
def max_milk(number_of_cows,max_weight,weight_of_cows,milk_of_cows):
    # Inicializamos la leche a obtener
    max_milk_obtainable = 0
    # Para cada número de vacas
    for i in range(number_of_cows):  
        # Para cada posible combinación de ellas  
        iterable= itertools.combinations(range(number_of_cows),i+1)
        for element in iterable:
            # Si la suma del peso es menor que el que soporta el camión
            if sum([weight_of_cows[i] for i in list(element)]) <= max_weight:
                # Si la cantidad que leche que producen al día es mayor que la anterior máxima
                if sum([milk_of_cows[i] for i in list(element)]) >= max_milk_obtainable:
                    # Guardar la cantidad de leche
                    max_milk_obtainable = sum([milk_of_cows[i] for i in list(element)])
    return max_milk_obtainable
    



if __name__ == "__main__":
    number_of_cows = int(input("Introduzca el número de vacas:\n"))
    max_weight = int(input("Introduzca el peso máximo del camión:\n"))
    weight_of_cows = [] 
    milk_of_cows = []
    for i in range(number_of_cows):
        weight_of_cows.append(int(input("Introduzca el peso de la vaca "+ str(i+1) + ":\n")))
    for i in range(number_of_cows):
        milk_of_cows.append(int(input("Introduzca la producción de leche da la vaca "+ str(i+1) + ":\n")))

    max_milk_obtainable = max_milk(number_of_cows,max_weight,weight_of_cows,milk_of_cows)
    print("The maximum number of milk is "+str(max_milk_obtainable))
    
            

