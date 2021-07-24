"""
Un entero se dice que es un palíndromo si es igual al número que se obtiene al invertir el orden de sus cifras. Por ejemplo, 79197 y 324423 son palíndromos. En esta tarea se le dará un entero N, 1 <= N <= 1.000.000. Usted debe encontrar el menor entero M tal que M <= N que es primo y M es un palíndromo N.

Por ejemplo, si N es 31, entonces la respuesta es 101.

Formato de entrada:
Un solo entero N, (1 <= N <= 1.000.000), en una sola línea.

Formato de salida:
Su salida debe consistir en un solo número entero, el más pequeño palíndromo primo mayor que o igual a N.
"""
"""
Testeo si es primo y si es es palíndromo para cada valor desde el que recibimos. se podría optimizar, pero como no se pide, el código es sencillo aunque tarde.
"""
from math import sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

def is_palindrome(n):
    return n == int(str(n)[::-1])

def encontrar_primo_palindromo(nummenor):
    i = nummenor
    while True:
        if is_prime(i) and is_palindrome(i):
            return i
        i = i+1


    return 0



if __name__ == "__main__":
    nummenor = input("Introduzca el número: ")
    
    result = encontrar_primo_palindromo(int(nummenor))
    
    print(result)


