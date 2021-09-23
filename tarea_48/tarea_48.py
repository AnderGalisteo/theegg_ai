"""
De una cadena dada de máximo 30 caracteres debéis construir una función 
que comprima la cadena mediante LZ77 y una función que la descomprima. Evidentemente el input y el 
output deben coincidir:
1.- Recoger el input de máximo 30 caracteres
2.- Hacer un print que informe sobre el espacio de memoría que ocupa el string introducido.
3.- Comprimir
4.- Hacer un print que informe sobre el espacio de memoría que ocupa el string comprimido.
5.- Descomprimir. El output debe ser igual que el input.
6.- Hacer un print que informe sobre el espacio de memoría que ocupa el string descomprimido. Una vez 
descomprimido debería tener el mismo peso que el original.
"""
"""
Podría intenar hacerlo todo a mano, pero la librería zlib lo puede hacer por mi.
"""

import zlib

if __name__ == "__main__":
    a = input("Enter the phrase\n") 
    if len(a) > 30:
        print("The maximum size should be 30 characters")
        exit()
    print("The original length is ", len(a))
    ac = zlib.compress(a.encode())
    print("The compressed length is ", len(ac))
    ad = zlib.decompress(ac).decode()
    print("The uncompressed length is ", len(ad))
    if a == ad:
        print("The two strings are equal!")
    else:
        print("The two strings are not equal!")


