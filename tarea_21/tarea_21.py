val = input("Introduzca su valor entre 0.0001 y 0.9999: ")
try:
    x = float(val)
except ValueError:
    print("Tiene que introducir un número")
    exit()
if len(val)>6:
    print("El número no puede tener más que 4 decimales")
    exit()
if not(x>= 0.0001 and x<=0.9999):
    print("El número tiene que estar entre 0.0001 y 0.9999")
    exit()
numerador = int(x*1000)
denominador = 1000

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

print(str(int(numerador))+"/"+str(int(denominador)))

