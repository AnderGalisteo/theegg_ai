"""
En este caso hay que desarrollar un programa donde una vez enviado un valor decimal a una función este lo convierta a binario y nos lo devuelva. Se trata de construir un simulador de un convertidor analógico digital mediante un programa (software). El hardware lo dejamos para otro día
"""
"""
Se nos dice que es un valor decimal pero no en que rango. Yo voy a coger un valor entre 0 y 1. 1 se mapeara a "11111111" equivalente a 255 y 0 a 0. 
Cualquier valor intermedio será interpretado proporcionalmente. Si el valor está fuera de rango, devolverá -1, un error.
Los "leading zeros" he decidido quitarlos, ya que así la solución es mś limpia en caso de números pequeños.
"""
def dec_a_binario(val):
    try:
        x = float(val)
    except ValueError:
        print("Tiene que introducir un número")
        return -1
    if not(x>= 0 and x<=1):
        print("El número tiene que estar entre 0 y 1")
        return -1
        
    return bin(int(x*255))[2:]



if __name__ == "__main__":
    val = input("Introduzca su valor entre 0 y 1: ")
    binvalue = dec_a_binario(val)
    if binvalue == -1:
        print("Un error ocurrio")
        exit()
    print(binvalue)

