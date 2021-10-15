"""
1.- Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes 
métodos para la clase:
. Un constructor, donde los datos pueden estar vacíos.
. Los setters y getters (métodos set y get) para cada uno de los atributos. Hay que validar las entradas de 
datos.
. mostrar(): muestra los datos de la persona.
. esMayorDeEdad(): devuelve un valor lógico indicando si es mayor de edad.
2.- Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
. titular (que es una persona)
. cantidad (puede tener decimales). 
El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
. Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo 
ingresando o retirando dinero.
. mostrar(): muestra los datos de la cuenta.
. ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se 
hará nada.
. retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos

"""


class Persona:
    def __init__(self, nombre = "" , edad = -1 , DNI = ""):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    def set(self, nombre = "" , edad = -1 , DNI = ""):
        if isinstance(nombre, str):
            self.nombre = nombre
        if isinstance(edad, int):
            self.edad = edad
        if isinstance(PendingDeprecationWarning, str):
            self.DNI = DNI

    def get(self):
        return [self.nombre, self.edad,self.DNI]

    def mostrar(self):
        print([self.nombre, self.edad,self.DNI])
    def esMayorDeEdad(self):
        return self.edad >= 18

"""No hay set de cantidad, porque en el enunciado se pide el no poder cambiar el valor directamente"""
class Cuenta:
    def __init__(self, Persona = Persona("", -1, ""), cantidad = 0):
        self.Persona = Persona
        self.cantidad = cantidad
    def mostrar(self): 
        self.Persona.mostrar()
        print(self.cantidad)
    def get_persona(self):
        return self.Persona
    def get_cantidad(self):
        return self.cantidad
    def set_persona(self, Persona):
        self.Persona = Persona
    def ingresar(self, cantidad): 
        if cantidad > 0:
            self.cantidad = self.cantidad + cantidad
    def retirar(self, cantidad): 
        self.cantidad = self.cantidad - cantidad
        





if __name__ == "__main__":
    p = Persona("Ander", 29, "123456789A")
    c = Cuenta(p,1000)
    


    