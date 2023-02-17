MENU = ["Salir", "Añadir alumno", "Buscar alumno", "Añadir nota alumno", "Mostrar la media de notas alumno", "Borrar un alumno"]
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


#print_menu(MENU)

def load_data():
    dic = {}
    f = open("Pt1UF3\\alumnos.txt", "r")
    for i in f:
        a = i.rsplit("-")
        dic[a[0]] = a[1].rstrip("\n").rsplit(" ")
    return dic

def get_nota(get_num=0):
    """
    Esta función pide al usuario un número y verifica unos requisitos necesarios por el programa.
    :return: Devuelve el número seleccionado
    """
    try:
        get_num = int(input("Introduce la primera nota del alumno: "))
    except ValueError:
        get_nota()
    return get_num


def export_data(alumnos_dic, op=1):
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
    alumno = input("Alumno que se desea añadir: ")
    if alumno not in alumnos_dic and alumno != "":
        alumnos_dic[alumno] = [f"{get_nota()}"]
        export_data(alumnos_dic)
    else:
        print("El alumno ya existe")
        add_alumno(alumnos_dic)


def add_nota(alumnos_dic):
    alumno = input("Alumno al que se le desea añadir nota: ")
    if alumno in alumnos_dic:
        alumnos_dic[alumno].append(f"{get_nota()}")
        export_data(alumnos_dic)
    else:
        print("El alumno introducido no existe.")
        add_nota(alumnos_dic)
        
    

def main_program(alumnos_dic, lista_menu):
    select = print_menu(lista_menu)
    if select == 0:
        exit("Has salido exitosamente del programa.")
    elif select == 1:
        add_alumno(alumnos_dic)
    elif select == 2:
        add_nota(alumnos_dic)
    elif select == 3:
        pass
    elif select == 4:
        pass
    elif select == 5:
        pass
    print(alumnos_dic)
    

alumnos = load_data()
main_program(alumnos, MENU)

