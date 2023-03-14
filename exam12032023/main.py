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


def create_players():
    """
    Función que crea y setea los datos a los jugadores
    :return: Devuelve los dos jugadores creados por este método
    """
    player1 = Jugador()
    player1.set_datos(1, "Carlos", 6, 7)
    player2 = Jugador()
    player2.set_datos(2, "Maria", 6, 7)
    return player1, player2


def pedir_tirada(jugador):
    """
    Función que pide la posición de la tirada a un jugador.
    :param jugador: Jugador al que se le va a pedir la tirada. 
    :return: Coordenadas en las que se va a realizar la tirada.
    """
    print(f"Usuario {jugador.nombre} es tu turno, elige las coordenadas en las que se va a disparar.")
    try:
        x = int(input("Posición x de la tirada: "))
        y = int(input("Posición y de la tirada: "))

        if (x < 0 or x > 4) or (y < 0 or y > 4):
            print("ERROR: El valor solo puede estar entre 0 y 4.")
            raise ValueError
    except ValueError:
        pedir_tirada(jugador)
    return x, y


def efectuar_tirada(player1, player2):
    """
    Función que analiza la tirada que ha especificado el jugador y la efectua, devolviendo en todo caso si se ha tocado agua o barco.
    :param player1: Objeto del jugador1
    :param player2: Objeto del jugador2
    """
    xpos, ypos = pedir_tirada(player1)
    test = player2.tablero.set_estado(xpos, ypos)
    if test == 0:   
        print(f"Se ha disparado en la posición: X = {xpos} | Y = {ypos} - Has tocado agua")
    elif test == 1:
        print(f"Se ha disparado en la posición: X = {xpos} | Y = {ypos} - Has tocado un barco")
        player2.barcos_restantes = player2.barcos_restantes - 1
    elif test == 2:
        print(f"Se ha disparado en la posición: X = {xpos} | Y = {ypos} - Has tocado una casilla que previamente ya habias tocado.")
    player1.num_tiradas = player1.num_tiradas - 1


def check_ganada_barcos(player1, player2):
    """
    Función que checkea si un jugador ha ganado al otro jugador derribandole todos los barcos
    :param player1: Objeto del jugador1
    :param player2: Objeto del jugador2
    """
    if player2.barcos_restantes == 0:
        exit(f"Al jugador {player2.nombre} le quedan 0 barcos en el tablero. ¡Jugador {player1.nombre} has ganado!")
    elif player1.barcos_restantes == 0:
        exit(f"Al jugador {player1.nombre} le quedan 0 barcos en el tablero. ¡Jugador {player2.nombre} has ganado!")


def check_final(player1, player2):
    """
    Función que checkea si un jugador ha ganado o empatado
    :param player1: Objeto del jugador1
    :param player2: Objeto del jugador2
    """
    if (player1.num_tiradas == 0 and player2.num_tiradas == 0) and (player1.barcos_restantes > 0 and player2.barcos_restantes > 0):
        exit("¡Se acabó el juego!\nAmbos jugadores se han quedado sin tiradas.")
    check_ganada_barcos(player1, player2)


def jugada_player(player1, player2):
    """
    Función que efectua una tirada e imprime los tableros del jugador.
    :param player1: Objeto del jugador1
    :param player2: Objeto del jugador2
    """
    player2.print_tablero()
    efectuar_tirada(player1, player2)
    player2.print_tablero()


def start_game(player1, player2):
    """
    Función que hace que el juego empiece.
    :param player1: Objeto del jugador1
    :param player2: Objeto del jugador2
    """
    jugada_player(player1, player2)
    check_ganada_barcos(player1, player2)
    input("Presiona enter para pasar al siguiente turno...")
    jugada_player(player2, player1)
    check_final(player1, player2)
    input("Presiona enter para pasar al siguiente turno...")


def main_program(player1, player2, select):
    """
    Función que ejecuta el programa principal.
    :param player1: Objeto del jugador1
    :param player2: Objeto del jugador2
    :param select: Selección del usuario
    """
    if select == 0: exit("Has salido correctamente.")
    elif select == 1:
        while True:
            start_game(player1, player2)
    else: print("Solo hay 2 opciones disponibles...")


select = print_menu(MENU)
player1, player2 = create_players()

main_program(player1, player2, select)

