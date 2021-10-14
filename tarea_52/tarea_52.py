"""
Ejercicios propuestos:
1.- Desarrolla un programa que sirva para:
- Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el 
número 0, el cual no debe guardarse.
- A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su 
primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
- Recorrer la lista para imprimir la sumatoria de todos los elementos.
- Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores 
que el número dado. Imprimir esta nueva lista, iterando por ella.
- Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una 
compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si 
la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]


2.- Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, 
finalizando al ingresar ?x?. A continuación, solicitar que ingrese los nombres de los alumnos de nivel 
secundario, finalizando al ingresar ?x?.
- Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.
- Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
- Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

"""


"""Para el primer ejercicio vamos a utilizar una lista, ya que es la más fácil de recorrer y se pide recorrer varias veces"""
def ejercicio_1(number_elements):    
    num_list = []
    print("Introduzca todos los números que quiera y 0 para terminar \n")
    while(True):
        x = int(input(""))
        if x == 0:
            break
        num_list.append(x)
    x = int(input("Introduzca un número a eliminar\n"))
    try:
        num_list.remove(x)
    except:
        print("El número no existe")
    sumatoria = 0
    for i in num_list:
        sumatoria = sumatoria + i
    print("La suma de todos los elementos es " + str(sumatoria))

    x = int(input("Introduzca otro número\n"))

    nueva_lista = []

    for i in num_list:
        if i < x:
            nueva_lista.append(i)
    
    for i in nueva_lista:
        print(i)
    
    tuplas = []
    for i in num_list:
        if (i, num_list.count(i)) not in tuplas:
            tuplas.append((i, num_list.count(i)))
    print(tuplas)

"""Ya que no se pide repeticiones, vamos a utilizar sets"""
def ejercicio_2(number_elements):
    return number_elements


if __name__ == "__main__":
    #ejercicio_1()
    nombresdeprimaria = set()
    print("Introduzca los nombres de los alumnos de primaria")
    while True:
        x = input()
        if x == "?x?":
            break
        nombresdeprimaria.add(x)

    nombresdesecundaria = set()
    print("Introduzca los nombres de los alumnos de secondaria")
    while True:
        x = input()
        if x == "?x?":
            break
        nombresdesecundaria.add(x)

    nombrestotal = nombresdeprimaria | nombresdesecundaria
    print("Los nombres en total son: ")
    for i in nombrestotal:
        print(i)
    
    nombresendos = nombresdeprimaria & nombresdesecundaria
    print("Los nombres en los 2 son: ")
    for i in nombresendos:
        print(i)

    nombresprimarianosecon = nombresdeprimaria - nombresdesecundaria
    print("Los nombres en primaria y no en secundaria son: ")
    for i in nombresprimarianosecon:
        print(i)
    
    


    