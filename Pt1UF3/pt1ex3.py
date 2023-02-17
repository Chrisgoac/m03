def print_menu(lista, select=10):
    """
    Función que imprime el menú y pide una opción al usuario
    :return: La opción deseada
    """
    print("\t...: Menu :...")
    for i in range(len(lista)):
        print(f"{i} - {lista[i]}")

    try:
        select = int(input("Selecciona una opción: "))
    except ValueError:
        print_menu(lista)

    if select > 5 or select < 0:
        print_menu(lista)
    return select


def load_data():
    """
    Función que carga los datos del alumnos.txt a un diccionario del programa.
    :return: Devuelve el diccionaro con los datos cargados
    """
    dic = {}
    f = open("Pt1UF3\\alumnos.txt", "r")
    for i in f:
        a = i.rsplit("-")
        dic[a[0]] = a[1].rstrip("\n").rsplit(" ")
    return dic


def get_nota():
    """
    Esta función pide al usuario un número y verifica unos requisitos necesarios por el programa.
    :return: Devuelve el número seleccionado
    """
    get_num = 100
    try:
        get_num = float(input("Introduce la nota del alumno: "))
        if get_num < 0 or get_num > 10:
            raise ValueError
    except ValueError:
        return get_nota()
    return get_num


def export_data(alumnos_dic, op=1):
    """
    Función que exporta los datos de un diccionaro al archivo alumnos.txt
    
    :param op: Integer que se usa para saber la posición.
    """
    lista_dic = list(alumnos_dic.keys())
    f = open("Pt1UF3\\alumnos.txt", "w")
    for i in range(len(lista_dic)):
        f.write(f"{lista_dic[i]}-")
        for j in alumnos_dic[lista_dic[i]]:
            if len(alumnos_dic[lista_dic[i]]) == op:
                f.write(f"{j}\n")
                op = 1
            else:
                f.write(f"{j} ")
                op = op+1
    f.close()
    

def add_alumno(alumnos_dic):
    """
    Función que permite añadir a un usuario al diccionario.
    :param alumnos_dic: Diccionario al que se va a añadir el usuario
    """
    alumno = input("Alumno que se desea añadir: ")
    if alumno == "X":
        main_program(alumnos_dic)
    if alumno not in alumnos_dic and alumno != "":
        alumnos_dic[alumno] = [f"{get_nota()}"]
        export_data(alumnos_dic)
    else:
        print("El alumno ya existe")
        add_alumno(alumnos_dic)


def add_nota(alumnos_dic):
    """
    Función que permite añadir una nota a un usuario del diccionario.
    :param alumnos_dic: Diccionario al que se va a la nota del usuario
    """
    alumno = input("Alumno al que se le desea añadir nota: ")
    if alumno == "X":
        main_program(alumnos_dic)
    if alumno in alumnos_dic:
        alumnos_dic[alumno].append(f"{get_nota()}")
        export_data(alumnos_dic)
    else:
        print("El alumno introducido no existe.")
        add_nota(alumnos_dic)
        

def get_alumno(alumnos_dic):
    """
    Función que permite ver las notas de un usuario.
    :param alumnos_dic: Diccionario en el que se van a consultar las notas.
    """
    alumno = input("Alumno que se desea buscar: ")
    if alumno == "X":
        main_program(alumnos_dic)
    if alumno in alumnos_dic:
        print(f"Notas del alumno {alumno}:" , end=" ")
        for i in alumnos_dic[alumno]:
            print(i, end=" ")
    else:
        print("El alumno introducido no existe.")
        get_alumno(alumnos_dic)


def get_media_alumno(alumnos_dic, total=0):
    """
    Función que permite saber la media de notas de un alumno.
    :param alumnos_dic: Diccionario en el que se va a consultar la media de notas del usuario.
    """
    alumno = input("Alumno del que se desea obtener la media: ")
    if alumno == "X":
        main_program(alumnos_dic)
    if alumno in alumnos_dic:
        print(f"Media de notas del alumno {alumno}:" , end=" ")
        for i in alumnos_dic[alumno]:
            total = total + int(i)
        print(f"{total / len(alumnos_dic[alumno])}")
    else:
        print("El alumno introducido no existe.")
        get_media_alumno(alumnos_dic)


def main_program(alumnos_dic):
    """
    Función principal del programa que llama a todas las demás funciones.
    :param alumnos_dic: Diccionario que usa el programa como BBDD.
    """
    MENU = ["Salir", "Añadir alumno", "Buscar alumno", "Añadir nota alumno", "Mostrar la media de notas alumno", "Borrar un alumno"]
    while True:
        select = print_menu(MENU)
        if select == 0:
            exit("Has salido exitosamente del programa.")
        elif select == 1:
            add_alumno(alumnos_dic)
        elif select == 2:
            get_alumno(alumnos_dic)
        elif select == 3:
            add_nota(alumnos_dic)
        elif select == 4:
            get_media_alumno(alumnos_dic)
        elif select == 5:
            pass
        print(alumnos_dic)
    

alumnos = load_data()
main_program(alumnos)

