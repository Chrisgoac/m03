def get_letter(dni):
    """
    Función que devuelve la letra de un DNI
    :param dni: DNI al que queremos obtener la letra.
    :return: letra del DNI 
    """
    LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"
    return LETRAS[dni % 23]


def tratar_dnis():
    """
    Función que trata los DNIs para que se nos quede en un formato legible.
    :return: Devuelve una lsita con los DNIs y su correspondiente letra.
    """
    lista2 = []
    f = open("Pt1UF3\\nums_dni.txt")
    lista = f.read().split()
    for i in lista:
        lista2.append(f"{i}-{get_letter(int(i))}")
    f.close()
    return lista2


def ask_filename():
    """
    Función que pregunta por el nombre del archivo que vamos a crear.
    :return: Nombre del archivo que se va a crear.
    """
    name = input("Escribe el nombre del archivo deseado para guardar los DNIs: ")
    return name


def add_to_txt_and_print(file):
    """
    Función que añade al archivo e imprime la lista de los DNIs.
    :param file: Nombre del archivo que se va a crear con los DNIs.    
    """
    lista = tratar_dnis()
    print("DNIs\n-----------")
    for i in lista:
        print(i)
    f = open(file, "w")
    for i in lista:
        f.write(f"{i}\n")

add_to_txt_and_print(ask_filename())