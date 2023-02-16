MENU_LIST = ["Salir", "Nuevo fichero con nombres", "Nuevo fichero con apellidos", "Nuevo fichero con nombres y apellidos (num letras solicitadas)", "Nuevo fichero con nombres y apellidos (empieza letra solicitada)"]
def print_menu(lista, select=10):
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

# Cuidado con la ruta, si no funciona al corregirlo es por esto.

def tratar_nombres(nombre_o_apellido):
    """
    Esta funcion abre un archivo con nombres y apellidos, trata los datos 
    y devuelve una lista con los nombres o los apellidos, según se seleccione.
    :param nombre_o_apellido: int en el que 0 = return de lista con los nombres | 1 = return de lista con apellidos.
    """
    lista = []
    f = open("Pt1UF3\personas.txt", "r")
    num_lines = len(f.readlines())
    f.seek(0)
    for i in range(num_lines):
        lista.append(f.readline().rstrip("\n").split(" ")[nombre_o_apellido])
    return lista

# Cuidado con la ruta, si no funciona al corregirlo es por esto.

def new_fnames():
    lista = []
    f = open("Pt1UF3\\nombres.txt", "w")
    lista = tratar_nombres(0)
    for i in lista:
        f.write(f"{i}\n")
    f.close() 

# Cuidado con la ruta, si no funciona al corregirlo es por esto.

def new_fapellidos():
    lista = []
    f = open("Pt1UF3\\apellidos.txt", "w")
    lista = tratar_nombres(1)
    for i in lista:
        f.write(f"{i}\n")
    f.close()


def get_numbers():
    try:
        get_num = int(input("Introduce el máximo número de carácteres que puede tener el nombre: "))
    except ValueError:
        get_numbers()
    return get_num


def new_fwithmaxnumber():
    lista = []
    get_num = get_numbers()
    f = open(f"Pt1UF3\\nombre_con_{get_num}_letras.txt", "w")
    lista = tratar_nombres(1)
    for i in lista:
        f.write(f"{i}\n")
    f.close()


def new_fapellidos():
    lista = []
    
    f = open("Pt1UF3\\nombre_con_{apellidos.txt", "w")
    lista = tratar_nombres(1)
    for i in lista:
        f.write(f"{i}\n")
    f.close()


def main_program(men_list):
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
        pass

main_program(MENU_LIST)
