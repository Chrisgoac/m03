"""
-----------------------------------------------------------
EJERCICIO 1  ----------------------------------------------
(2 puntos)

- Pedir al usuario su nombre y su DNI sin letra.
- Mostrar todos los datos en forma de tabla.
- Que el programa nos pida cuantos DNI queremos añadir
-
                    Usuarios
                    ---------
                    Nombre --> XXXXXXXX-X
"""

DNIs = []
LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"


def return_dni(dni, letras):
    """
    Función que nos dice la letra del DNI que hemos introducido
    :param dni: DNI del usuario, solo números
    :param letras: Las posibles letras que puede tener un DNI
    :return: Devuelve la letra del DNI correcta.
    """
    return letras[dni % 23]


def print_resultado(lista, letras):
    """
    Función que imprime el DNI con su letra, previamente calculando la misma usando otra función.
    :param lista: Lista de DNIs de usuarios, serán utilizados para calcular su letra e imprimirla por pantalla
    :param letras: Lista de letras disponibles DNI
    :return:
    """
    print("Usuarios\n-------------")
    for i in range(len(lista)):
        print(f"{lista[i][0]} ----> {lista[i][1]}-{return_dni(lista[i][1], letras)}")


def check_nombre(name):
    """
    Función que verifica que el nombre no esté vacio
    :param name: Nombre que se ha introducid
    :return: Devuelve true o false en función de si está vacio o no
    """
    if name == "":
        print("El nombre no puede estar vacio.")
        return False
    else:
        return True


def check_dni(dni):
    """
    Función que checkea que un DNI sea válido.
    :param dni:
    :return: Devuelve True o False
    """
    try:
        dni = int(dni)
        if len(str(dni)) != 8:
            raise ValueError
    except (ValueError, TypeError) as err:
        print(err)
        print("El formato del DNI no es correcto")
        return False
    return True


def start_program(num_dnis, letras, dnis, count):
    """
    Función que inicia el programa
    :param num_dnis: Num de DNIs deseados
    :param letras: Lista que contiene las letras de los DNI
    :param dnis: Lista que guarda los DNIs y el nombre de la persona
    :param count: Parámetro que actua de contador para saber si el número deseado de DNIs ya se ha añadido.
    :return:
    """
    while count < num_dnis:
        name = input("Introduce tu nombre: ")
        if not check_nombre(name):
            continue
        dni = input("Introduce tu DNI sin letra: ")
        if not check_dni(dni):
            continue
        lista_vacia = [name, int(dni)]
        dnis.append(lista_vacia)
        count += 1
    print_resultado(dnis, letras)


while True:
    dnis_num = int(input("Numero de DNIs que deseas agregar: "))
    if dnis_num < 1:
        continue
    start_program(dnis_num, LETRAS, DNIs, 0)
    break

