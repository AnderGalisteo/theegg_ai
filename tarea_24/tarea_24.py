"""
Según la definición de google un algoritmo es: "Un conjunto ordenado de operaciones sistemáticas que permite hacer un cálculo y 
hallar la solución de un tipo de problemas".En esta tarea debes desarrollar (en el lenguaje o lenguajes de programación que tú 
quieras) el siguiente algoritmo:Un programa que dado un número introducido entre 0,0001 y 0,9999 (no más de 4 cifras decimales), 
obtenga y muestre la correspondiente fracción irreducible.Por ejemplo, el número 0,25 se puede obtener a partir de 25/100, o de 2/8, 
o de 1/4, entre otros. La fracción irreducible es 1/4, que está formada por un numerador y un denominador que son primos entre sí.
"""
"""
Lo he programado en python y el algoritmo es muy sencillo. Intenta dividir por 2 y luego por 3 etc hasta que encuentre un número por 
el que dividirlo o llegue hasta el mínimo entre el numerador y el denominador.
"""
def verificar_y_calcular(val):
    try:
        x = float(val)
    except ValueError:
        print("Tiene que introducir un número")
        return 1,0
    if len(val)>6:
        print("El número no puede tener más que 4 decimales")
        return 2,0
    if not(x>= 0.0001 and x<=0.9999):
        print("El número tiene que estar entre 0.0001 y 0.9999")
        return 3,0
    numerador = int(x*10000)
    denominador = 10000

    maxnum = min(numerador, denominador)

    i = 2
    while(i<=maxnum):
        if numerador%i == 0 and denominador%i == 0:
            numerador = numerador/i
            denominador = denominador/i
            maxnum = min(numerador, denominador)
            i = 2
        else:
            i = i + 1
    return str(int(numerador)), str(int(denominador))



if __name__ == "__main__":
    val = input("Introduzca su valor entre 0.0001 y 0.9999: ")
    numerador, denominador = verificar_y_calcular(val)
    if not(denominador == 0):
        print(numerador+"/"+denominador)

