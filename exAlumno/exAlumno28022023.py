"""
Crearemos un objeto Alumno (mediante su propia clase) que tendrá los atributos:
    id: int
    nombre: str
    edad: int
    altura: int
    modulos: List

Deberemos tener un constructor que nos permita crear un objeto vacio y un metodo con la introducción de los datos por parametro.
Crearemos el metodo "ToString" que devolvera un string con todos los datos encadenados.
Todos los atributos seran privados, excepto los modulos, que si seran publicos. Es decir, no podremos acceder a ningun atributo, salvo
la excepcion, directamente. Ni para mostrarlo ni para editarlo.



Haremos un menu que nos pedira si queremos introducir los datos por el usuario o de forma automatica.
En caso de elegir de forma automatica, crearemos los datos por el parametro.
En caso de elegir la entrada por usuario, le iremos pidiendo los datos a nuestro usuario:
    - La edad debera ser +18 o avisara al usuari
    - Tiene que haber minimo 1 modulo
    - El ID será menor de 10.
    - Nadie puede llamarse "Pepe"

Será la clase la que controlará estos limites.
La clase deberá estar en fichero separado de nuestro main.

"""

class Alumno:

    def __init__(self):
        self.__id = None
        self.__nombre = None
        self.__edad = None
        self.__altura = None
        self.modulos = None


    def load_data(self, id, nombre, edad, altura, modulos):
        self.__id = id
        self.__nombre = nombre
        self.__edad = edad
        self.__altura = altura
        self.modulos = modulos


    def get_id(self):
        return self.__id

    def set_id(self, valor):
        if valor >= 10:
            pass
        else:
            self.__id = valor

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, valor):
        if valor == "Pepe":
            pass
        else:
            self.__nombre = valor

    def get_edad(self):
        return self.__edad

    def set_edad(self, valor):
        if valor < 18:
            pass
        else:
            self.__edad = valor

    def get_altura(self):
        return self.__altura

    def set_altura(self, valor):
        self.__altura = valor

    def get_modulos(self):
        return self.__modulos

    def set_modulos(self, valor):
        self.__modulos = valor

    def to_string(self):
        return f"Alumno {self.__nombre} con ID {self.__id} tiene {self.__edad} años, mide {self.__altura}cm y tiene los módulos {self.__modulos}."



