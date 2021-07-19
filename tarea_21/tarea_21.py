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

    maxnum = max(numerador, denominador)

    i = 2
    while(i<maxnum):
        if numerador%i == 0 and denominador%i == 0:
            numerador = numerador/i
            denominador = denominador/i
            maxnum = max(numerador, denominador)
            i = 2
        else:
            i = i + 1
    return str(int(numerador)), str(int(denominador))



if __name__ == "__main__":
    val = input("Introduzca su valor entre 0.0001 y 0.9999: ")
    numerador, denominador = verificar_y_calcular(val)
    if not(denominador == 0):
        print(numerador+"/"+denominador)

