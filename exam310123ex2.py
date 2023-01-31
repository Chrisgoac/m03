"""
-----------------------------------------------------------
EJERCICIO 2  ----------------------------------------------
-----------------------------------------------------------
(4 puntos)

Haremos un menú con las siguientes opciones: Salir, Crear BBDD, Crear 1 elemento BBDD
Consultar toda la BBDD, Consultar 1 elemento BBDD, Eliminar elemento BBDD

base_datos = [
                ["ID",
                "Nombre",
                "Teléfono",
                "Fecha Nacimiento"]
                ]


- Crear BBDD: Generara un conjunto de datos para nuestra base de datos con 4 personas diferentes,
con 4 ID, 4 nombres...etc.
- Añadir 1 elemento: Pedir al usuario los datos y añadir un nuevo elemento a nuestra base de datos
- Consultar base de datos: Mostrar la base de datos en formato tabla:

BBDD
----
ID - Nombre - ...
ID - Nombre - ...



- Consultar un elemento: Pedir al usuario un ID, y mostrar todos sus datos:
ID: ----
Nombre: -----
...

- Eliminar elemento: pedir un ID, mostrar los datos y solicitar confirmación del borrado.
ID: ----
Nombre: -----
...
¿Desea eliminar el elemento?
"""

MENU = ["Salir", "Crear BBDD", "Crear 1 elemento BBDD", "Consultar toda la BBDD", "Consultar 1 elemento BBDD",
        "Eliminar elemento BBDD"]

SAMPLE_ID = [1, 2, 3, 4]
SAMPLE_NAME = ["Pepe", "Carlos", "Pepa", "Carla"]
SAMPLE_TELF = ["611111111", "622222222", "633333333", "644444444"]
SAMPLE_DATE = ["01/02/2004", "01/02/2005", "01/02/2006", "01/02/2007"]

database = []


def print_list(lst):
    """

    :param lst:
    :return:
    """
    print("\t...:Menu:...")
    for i in range(len(lst)):
        print(f"{i} - {lst[i]}")


def create_bbdd(dtb, id, name, telf, date):
    """
    Crea la base de datos con datos qde ejemplo
    :param dtb: Lista que actua de base de datos
    :param id: Lista para ID de ejemplo
    :param name: Lista para name de ejemplo
    :param telf: Lista para telf de ejemplo
    :param date: Lista para date de ejemplo
    :return:
    """
    for i in range(len(SAMPLE_ID)):
        lst_add = [id[i], name[i], telf[i], date[i]]
        dtb.append(lst_add)
    return dtb


def print_all_database(dtb):
    """
    Imrpime toda la base de datos
    :param dtb: Lista que actua de base de datos
    :return:
    """
    for i in range(len(dtb)):
        print(f"{dtb[i][0]} - {dtb[i][1]} - {dtb[i][2]} - {dtb[i][3]}")


def create_element(dtb):
    """
    Crea un elemento que se añadirá a la base de datos
    :param dtb: Lista que actua de base de datos
    :return:
    """
    name = input("Nombre: ")
    telf = input("Teléfono: ")
    date = input("Fecha de nacimiento: ")

    lista_vacia = [len(dtb[0]) + 1, name, telf, date]
    dtb.append(lista_vacia)
    return database


def check_database_index(dtb):
    """
    Imprime una entrada en la base de datos
    :param dtb: Lista que actua de base de datos
    :return:
    """
    try:
        index = int(input("Elemento al cual se quiere acceder de la BBDD: "))
        if index > len(dtb):
            raise ValueError
        print(f"Nombre: {dtb[index - 1][1]}\nTeléfono: {dtb[index - 1][2]}\nFecha de nacimiento: {dtb[index - 1][3]}\n")
    except ValueError:
        print("ERROR!")


def erase_database_index(dtb):
    """
    Elimina un valor de la base de datos
    :param dtb: Lista que actua de base de datos
    :return: Devuelve la base de datos
    """
    try:
        index = int(input("Elemento al cual se quiere eliminar de la BBDD: "))
        if index > len(dtb):
            raise ValueError
        dtb.pop(index-1)
        return dtb
    except ValueError:
        print("ERROR!")

def main_program(dtb):
    """
    Función que ejecuta all el código del programa
    :param dtb: Lista que actua de base de datos
    :return:
    """
    while True:
        print_list(MENU)
        select = 999
        try:
            select = int(input("Selecciona la opción: "))
        except ValueError:
            print("ERROR!")
        if select == 0:
            print("Has salido del programa.")
            break
        elif select == 1:
            dtb = create_bbdd(dtb, SAMPLE_ID, SAMPLE_NAME, SAMPLE_TELF, SAMPLE_DATE)
            continue
        elif select == 2:
            dtb = create_element(dtb)
        elif select == 3:
            print_all_database(dtb)
        elif select == 4:
            check_database_index(dtb)
        elif select == 5:
            dtb = erase_database_index(dtb)
        else:
            print("Option not available")


main_program(database)
