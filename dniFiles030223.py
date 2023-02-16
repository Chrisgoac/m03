# Pedir 3 DNI al usuario sin letra
# Inscribirlos en un aechivo

LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"
dnis = []
FICHERO_NAME = "fichero.txt"
MENU_LIST = ["Salir", "Crear fichero", "Añadir 3 DNIs", "Vaciar fichero", "Eliminar último DNI"]

def print_and_select(lista):
    print("\t...:Menu:...")
    for i in range(len(lista)):
        print(f"{i} - {lista[i]}")
    try:
        select = int(input("Opción de la lista deseada: "))
    except ValueError:
        print("ERROR!")
        print_and_select(lista)
    return select


def main_program(sel, lista, name):
    if sel == 0:
        exit()
    elif sel == 1:
        crear_fichero(FICHERO_NAME)
    elif sel == 2:
        pass
    elif sel == 3:
        pass
    elif sel == 4:
        pass
    else:
        print("Código no válido.")
        print_and_select(lista)


def crear_fichero(name):
    f = open(name, "w")
    f.close()


def pedir_dni(lista, letras, contador=0):
    if contador < 3:
        dni = int(input("Introduce el DNI: "))
        lista.append(str(dni) + str(get_letra(dni, letras)))
        return pedir_dni(lista, letras, contador + 1)
    else:

        return lista


def get_letra(dni, lista):
    return str(lista[dni % 23])


def add_to_file(lista, name):
    f = open(name, 'a')
    for i in lista:
        f.write(f"{i}\n")
    f.close()


selection = print_and_select(MENU_LIST)
main_program(selection, MENU_LIST, FICHERO_NAME)


print(dnis)
