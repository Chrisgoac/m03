from Jugador import Jugador

MENU = ["Salir", "Jugar"]

def print_menu(men):
    """
    Funcion que imprime un menu y pide al usuario una opción
    :param menu: Argumento que actua de lista para imprimir el menu.
    :return: Devuelve la opción introducida por el usuario
    """
    print(f"\t...:Menu:...")
    for i in range(len(men)):
        print(f"{i} - {men[i]}")
    print()

    try:
        select = int(input("Selecciona la opción: "))
        return select
    except ValueError:
        print_menu(men)

select = print_menu(MENU)

player1 = Jugador()
player1.set_datos(1, "Carlos", 6)
player2 = Jugador()
player2.set_datos(2, "Maria", 6)

if select == 0:
    exit("Has salido correctamente.")
elif select == 1:
    

    player1.tablero.print_tablero()
else:
    print("ERES IMBECIL, SOLO TIENES 2 OPCIONES")

def pedir_tirada(jugador):
    print(f"Usuario {jugador.nombre} es tu turno")
    x = int(input("Posición x de la tirada: "))
    y = int(input("Posición y de la tirada: "))
    return x, y


def pedir_tirada_get_result(player1, player2):
    xpos, ypos = pedir_tirada(player)
    test = player.tablero.set_estado(xpos, ypos)
    if test == 0:   
        print("Has tocado agua")
    elif test == 1:
        print("Has tocado un barco")
    elif test == 2:
        print("ERES IMBECIL")


pedir_tirada_get_result(player1)


