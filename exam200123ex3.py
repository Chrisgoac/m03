import random as rand

"""
-----------------------------------------------------------
EJERCICIO 3 ----------------------------------------------
-----------------------------------------------------------
(3 puntos)
Realizaremos un programa que jugará al 3 en raya. Nuestro programa nos informará
de que el juego empieza, nos mostrará el tablero vacío y empezará a jugar la IA.
Solo se hará 3 en raya si las 3 filas iniciales, del medio o últimas, contienen
las piezas. El juego continuará mientras no se den estas condiciones o hasta un
máximo de 6 tiradas.
El método recursivo será el del juego, y se volverá a llamar a sí mismo para
seguir jugando mientras no se den las condiciones anteriormente descritas.
TABLERO INICIAL
O O O
O O O
O O O

O O O
X X X
O O O
Este sería un ejemplo de fin del juego.
"""

TABLERO = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]


def check_three(tablero):
    """
    Función que comprueba si se ha efectuado algún 3 en ralla.
    :param tablero: Lista que actuará de tablero de nuestro juego (en esta función la usamos para comprobar el tres en ralla)
    :return:
    """
    if tablero[0][0] == "X" and tablero[0][1] == "X" and tablero[0][2] == "X" or tablero[1][0] == "X" and tablero[1][
        1] == "X" and tablero[1][2] == "X" or tablero[2][0] == "X" and tablero[2][1] == "X" and tablero[2][2] == "X":
        print("El juego ha terminado, se ha producido un tres en ralla.")
        return True
    else:
        return False


def random_xy():
    """
    Función que devuelve dos ints con valor aleatorio.
    :return: Devuelve x e y, que usaremos como coordenadas
    """
    x = rand.randint(0, 2)
    y = rand.randint(0, 2)

    return x, y


def print_tablero(tablero):
    """
    Función que imprime el tablero correctamente formateado.
    :param tablero: Lista que actuará de tablero de nuestro juego.
    :return:
    """
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end=" ")
        print()


def start_game(tablero):
    """
    Función principal del juego
    :param tablero: Lista que actuará de tablero de nuestro juego
    :return:
    """
    x, y = random_xy()

    if not check_three(tablero):
        if tablero[x][y] == "O":
            tablero[x][y] = "X"
            input("Presiona ENTER para efectuar la siguiente tirada...")
            print_tablero(tablero)
        start_game(tablero)


print("El juego de 3 en ralla va a empezar\n")
print_tablero(TABLERO)
start_game(TABLERO)
