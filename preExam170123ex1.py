"""
EJERCICIO 3: HUNDIR LA FLOTA ------------------------------

El código va a crear un tablero de 4x4 y va a colocar 2 barcos en él. El código debe permitir, fácilmente, cambiar
la posición de los barcos antes de lanzar el programa.

# Antes de empezar a jugar:
- Creamos un tablero de 4x4 vacío ('A')
- Colocamos 2 barcos (posición con 'B'), uno de 2 celdas y otro de 3 celdas (horizontal o vertical pero que no solapen)

# Al iniciar el programa...
- Mostrar el menú de juego (diccionario o lista) y tablero inicial con los barcos:
        1 - Jugar
        0 - Salir
- En random, hacemos tiradas:
    - devolver posición de la tirada
    - devolver agua (cambiar la casilla vacía 'A' por 'X') o tocado (cambiar la casilla de barco 'B' por 'T')
    - devolver estado del tablero
    - Esperar 'ENTER' para siguiente tirada
- Al completar 6 tiradas, deberemos devolver un mensaje según si hemos conseguido hundir todos los barcos o no

EJEMPLO DEL 1ER TURNO ----------------------------------------------------
-  Mostramos el tablero al empezar el juego:
           0 1 2 3
         0 A B B A
         1 A A A B
         2 A A A B
         3 A A A B

- Vemos las posiciones del disparo:
    Se dispara en la posicion x: 0 y: 1
    Tocado!

- Mostramos el tablero con las modificaciones:
           0 1 2 3
         0 A T B A
         1 A A A B
         2 A A A B
         3 A A A B
- Esperamos al siguiente turno:   "Pulsa ENTER para continuar..."

INSTRUCCIONES:

	No se permitirán prints innecesarios ni dentro de condicionales ni iteraciones, salvo que sean necesarios
	No se permite el uso de métodos o funciones que no se han expuesto en clase
	Se entregarán tanto archivos como ejercicios tenga la prueba
	No se evaluará código comentado
	No se valorarán métodos/funciones de + 10 líneas.
	El programa principal podrá tener también un máximo de 10 líneas. Con excepción de encadenamientos de elif y las
líneas de control de errores, que no contarán para este limite.
	Controlar los errores que se puedan producir FUERA de los métodos/funciones. El programa NO puede fallar.
	Todos los métodos deberán estar comentados como se expuso en clase:
---------------------------------------------------------------------------------------------------
"""
import random


def print_menu(menu):
    """
    Función que imprime una lista en forma de menú
    :param menu: Lista que va a ser imprimida en forma de menú
    :return:
    """
    print("\t...:Menu:...")
    for i in range(len(menu)):
        print(f"{i} - {menu[i]}")


ships = 5
tiradas = 15

MAIN_MENU = ["Salir", "Jugar"]

SHIP1 = [[0, 0], [0, 1]]
SHIP2 = [[3, 1], [3, 2], [3, 3]]

tablero_game = [[" ", "0", "1", "2", "3"], ["0", "A", "A", "A", "A"], ["1", "A", "A", "A", "A"],
                ["2", "A", "A", "A", "A"],
                ["3", "A", "A", "A", "A"]]


def ship_position(barco1, barco2, tablero):
    """
    Función que posiciona los barcos dentro de un tablero vacio
    :param barco1: Lista que contiene la posición del barco 1.
    :param barco2: Lista que contiene la posición del barco 2.
    :param tablero: Lista que actua de tablero, en ella será reemplazada el agua por las posiciones de los barcos.
    :return:
    """
    for i in range(len(barco1)):
        tablero[barco1[i][0] + 1][barco1[i][1] + 1] = "B"

    for i in range(len(barco2)):
        tablero[barco2[i][0] + 1][barco2[i][1] + 1] = "B"


def print_tablero(tablero):
    """
    Función que te imprime una lista en forma de tablero.
    :param tablero: Lista que actua de tablero para ser imprimida por pantalla
    :return:
    """
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end=" ")
        print()


def touch_water(posX, posY, tablero):
    """
    Función que edita nuestro contador al tocar agua.
    :param tablero: Tablero en el que se efectua la tirada.
    :param posX: Posición X de la tirada
    :param posY: Posición Y de la tirada
    :return:
    """
    print(f"Se ha tocado agua en la posición: X: {posX - 1} | Y: {posY - 1}\n")
    tablero[posX][posY] = "X"
    print_tablero(tablero)
    input("Presiona ENTER para continuar...")


def touch_ship(posX, posY, tablero):
    """
    Función que edita nuestro contador al tocar un barco.
    :param tablero: Tablero en el que se efectua la tirada.
    :param posX: Posición X de la tirada
    :param posY: Posición Y de la tirada
    :return:
    """
    print(f"Se ha tocado un barco en la posición: X: {posX - 1} | Y: {posY - 1}\n")
    tablero[posX][posY] = "T"
    print_tablero(tablero)
    input("Presiona ENTER para continuar...")


def game_lost(tiradas_num):
    """
    Función que detecta si hemos perdido el juego.
    :param tiradas_num: Número de tiradas restantes
    :return:
    """
    if tiradas_num <= 0:
        print("Te has quedado sin tiradas.")
        return True


def game_won(barcos_num):
    """
    Función que detecta si hemos ganado el juego.
    :param barcos_num: Número de barcos restantes
    :return:
    """
    if barcos_num <= 0:
        print("Has aniquilado a todos los barcos, ¡felicidades!")
        return True


def random_xy():
    """
    Función que devuelve dos ints con valor aleatorio.
    :return:
    """
    x = random.randint(1, 4)
    y = random.randint(1, 4)

    return x, y


def start_game(barcos_num, tiradas_num, tablero):
    """
    Función para empezar el juego de hundir la flota
    :param barcos_num: Número de barcos restantes
    :param tiradas_num: Número de tiradas restantes
    :param tablero: Lista que actua de tablero
    :return:
    """
    if not game_lost(tiradas_num):
        x, y = random_xy()

        if not game_won(barcos_num):
            if tablero[x][y] == "X" or tablero[x][y] == "T":
                start_game(barcos_num, tiradas_num, tablero)
            if tablero[x][y] == "A":
                touch_water(x, y, tablero)
                start_game(barcos_num, tiradas_num - 1, tablero)
            elif tablero[x][y] == "B":
                touch_ship(x, y, tablero)
                start_game(barcos_num - 1, tiradas_num - 1, tablero)


def start_program(barcos_num, tiradas_num, tablero, barco1, barco2):
    print_menu(MAIN_MENU)
    try:
        select = int(input("\nSelecciona una opción: "))

        if select > 1 or select < 0:
            raise Exception

        if select == 0:
            print("Has salido del programa.")
        elif select == 1:
            ship_position(barco1, barco2, tablero)
            print_tablero(tablero)
            start_game(barcos_num, tiradas_num, tablero)
    except:
        print("Esa opción no es válida, selecciona un número del 0 al 1.")
        start_program(ships, tiradas, tablero_game)


start_program(ships, tiradas, tablero_game, SHIP1, SHIP2)
