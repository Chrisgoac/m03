"""
-----------------------------------------------------------
EJERCICIO 1 ----------------------------------------------
-----------------------------------------------------------
(3 puntos)
- Pedir al usuario su nombre y su DNI sin letra.
- Un método recursivo debe acabar asignando la letra correcta al DNI introducido.
- La recursividad deberá recorrer la lista de posibles letras.
- Mostrar todos los datos en forma de tabla.
Usuario
---------
Nombre --> XXXXXXXX-X
Las letras son: TRWAGMYFPDXBNJZSQVHLCKE
Y las letras se relacionan del 0 al 22:
0 = T
1 = R
2 = W
etc...
"""


DNIs = [["Christian", 54030317], ["Adolfo", 54030318], ["Eustaquio", 54030319], ["Manolo", 54030320], ["Estefania", 54030321], ["Juana", 54030322], ["Rigoberta", 54030323], ["Faustina", 54030324]]
LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"


def check_dni(dni, letras, selector=0):
    """
    Función que nos dice la letra del DNI que hemos introducido
    :param selector: Contador que nos permite lleavr un control del indice al que queremos acceder
    :param dni: DNI del usuario, solo números
    :param letras: Las posibles letras que puede tener un DNI
    :return: Devuelve la letra del DNI correcta.
    """
    if letras[0] != letras[(dni % 23) - selector]:
        letras = letras[1:]
        return check_dni(dni, letras, selector+1)
    else:
        return letras[0]


def print_resultado(lista, letras):
    """
    Función que imprime el DNI con su letra, previamente calculando la misma usando otra función.
    :param lista: Lista de DNIs de usuarios, serán utilizados para calcular su letra e imprimirla por pantalla
    :param letras: Lista de letras disponibles DNI
    :return:
    """
    print("Usuarios\n-------------")
    for i in range(len(lista)):
        print(f"{lista[i][0]} ----> {lista[i][1]}-{check_dni(lista[i][1], letras)}")


print_resultado(DNIs, LETRAS)
