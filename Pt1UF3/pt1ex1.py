MENU_LIST = ["Salir", "Nuevo fichero con nombres", "Nuevo fichero con apellidos", "Nuevo fichero con nombres y apellidos (num letras solicitadas)", "Nuevo fichero con nombres y apellidos (empieza letra solicitada)"]
def print_menu(lista, select=10):
    """
    Función que imprime el menú y pide una opción al usuario
    :return: La opción elegida
    """
    print("\t...: Menu :...")
    for i in range(len(lista)):
        print(f"{i} - {lista[i]}")

    try:
        select = int(input("Selecciona una opción: "))
    except ValueError:
        print_menu(lista)

    if select > 4 or select < 0:
        print_menu(lista)
    return select

# Cuidado con la ruta en las funciones, estoy usando una subcarpeta para mantener el orden, si no funciona al corregirlo es por esto.

def tratar_nombres(nombre_o_apellido):
    """
    Esta funcion abre un archivo con nombres y apellidos, trata los datos 
    y devuelve una lista con los nombres o los apellidos, según se seleccione.
    :param nombre_o_apellido: int en el que 0 = return de lista con los nombres | 1 = return de lista con apellidos.
    :return: Lista con los nombres o apellidos tratados.
    """
    lista = []
    f = open("Pt1UF3\personas.txt", "r")
    num_lines = len(f.readlines())
    f.seek(0)
    for i in range(num_lines):
        lista.append(f.readline().rstrip("\n").split(" ")[nombre_o_apellido])
    return lista


def new_fnames():
    """
    Esta función crea el archivo nombres y añade solo los nombres en dicho archivo.
    """
    lista = []
    f = open("Pt1UF3\\nombres.txt", "w")
    lista = tratar_nombres(0)
    for i in lista:
        f.write(f"{i}\n")
    f.close() 


def new_fapellidos():
    """
    Esta función crea el archivo apellidos y añade solo los apellidos en dicho archivo.
    """
    lista = []
    f = open("Pt1UF3\\apellidos.txt", "w")
    lista = tratar_nombres(1)
    for i in lista:
        f.write(f"{i}\n")
    f.close()


def get_numbers():
    """
    Esta función pide al usuario un número y verifica unos requisitos necesarios por el programa.
    :return: Devuelve el número seleccionado
    """
    try:
        get_num = int(input("Introduce el máximo número de carácteres que puede tener el nombre: "))
    except ValueError:
        get_numbers()
    return get_num


def get_letter():
    """
    Esta función pide al usuario una letra y verifica unos requisitos necesarios por el programa.
    :return: Devuelve la letra seleccionada
    """
    # Por motivos logísticos, asumimos que los nombres que empiezan con tilde no están aceptados en España :)
    verificar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ"
    get_num = str(input("Introduce la letra por la que deberán empezar los nombres: "))
    
    if len(get_num) != 1 or get_num not in verificar:
        get_letter()
    return get_num


def ret_lnames_lapellidos():
    """
    Función que devuelve los apellidos y los nombres por separado.
    :return: Se devuelven dos listas, una con los nombres y otra con los apellidos.
    """
    lista1 = tratar_nombres(0)
    lista2 = tratar_nombres(1)
    return lista1, lista2


def new_fwithmaxnumber():
    """
    Función que pregunta y crea un archivo con los nombres que tengan como mucho x letras.
    """
    nombres, apellidos = ret_lnames_lapellidos()
    get_num = get_numbers()
    f = open(f"Pt1UF3\\nombre_con_{get_num}_letras.txt", "w")
    for i in range(len(nombres)):
        if len(nombres[i]) <= get_num:
            f.write(f"{nombres[i]} {apellidos[i]}\n")
    f.close()


def new_fstartwithletter():
    """
    Función que pregunta y crea un archivo con los nombres que empiecen por x letra.
    """
    nombres, apellidos = ret_lnames_lapellidos()
    get_letra = get_letter()
    f = open(f"Pt1UF3\\nombre_start_letra_{get_letra}.txt", "w")
    for i in range(len(nombres)):
        if nombres[i][0] == get_letra:
            f.write(f"{nombres[i]} {apellidos[i]}\n")
    f.close()


def main_program(men_list):
    """
    Función que ejecuta el programa principal
    """
    select = print_menu(men_list)
    if select == 0:
        exit("Has salido del programa exitosamente.")
    elif select == 1:
        new_fnames()
    elif select == 2:
        new_fapellidos()
    elif select == 3:
        new_fwithmaxnumber()
    elif select == 4:
        new_fstartwithletter()

main_program(MENU_LIST)
