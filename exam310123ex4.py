
"""
-----------------------------------------------------------
EJERCICIO 4  ----------------------------------------------
-----------------------------------------------------------
(2 puntos)

Dadas las listas:
lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1]
lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 0]
]

4.1 - Compararemos ambas listas, mostrando por pantalla cuál de las 2 es mas larga.

4.2 - Realizaremos la media de cada una, indicando el resultado y cuál tiene la media más grande.

4.3 - Recorreremos la lista 1 y compararemos cada elemento de la lista, con el que tenga la misma posición de la otra. Indicando que lista posee el elemento con un valor más pequeño.

4.4 - Ordenaremos ambas listas de la misma forma y las mostraremos una de mayor a menor y la otra al revés de forma invertida.
"""

lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1]
lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 0]

print("EJERCICIO 4.1:")

def larger_list(list1, list2):
    """
    Checkea la lista que la suma total sea más grande
    :param list1: Lista 1
    :param list2: Lista 2
    :return:
    """
    if len(list1) > len(list2):
        print("La lista 1 es más larga")
    elif len(list2) > len(list1):
        print("La lista 2 es más larga")
    else:
        print("Las listas son iguales")


larger_list(lst1, lst2)

print("\nEJERCICIO 4.2:\n")

def sumar_lista(lst):
    """
    Función que suma los integers de una lista
    :param lst: Lista que va a ser sumada
    :return: Retorna el valor total de la lista
    """
    total = 0
    for i in lst:
        total += i
    return total


def check_media(list1, list2):
    """
    Checkea que lista tiene el valor medio más grande
    :param list1: Lista 1
    :param list2: Lista 2
    :return:
    """
    media_lst1 = sumar_lista(lst1)
    media_lst2 = sumar_lista(lst2)
    print(f"Media lista 1: {media_lst1}")
    print(f"Media lista 2: {media_lst2}\n")
    if media_lst1 > media_lst2:
        print("La media de la lista 1 es mayor")
    elif media_lst2 > media_lst1:
        print("La media de la lista 2 es mayor")
    else:
        print("Las medias de las listas son iguales")


check_media(lst1, lst2)


print("\nEJERCICIO 4.3:\n")

def check_larger_num(list1, list2):
    """
    Checkea cada elemento de la lista 1 con el elemento de la misma posición en la lista 2, imprimiendo cual es mayor.
    :param list1: Lista 1
    :param list2: Lista 2
    :return:
    """
    for i in range(len(list1)):
        if list1[i] > list2[i]:
            print(f"El elemento de la lista 2 es menor que el de la lista 1 ({list1[i]} > {list2[i]})")
        elif list2[i] > list1[i]:
            print(f"El elemento de la lista 1 es menor que el de la lista 2 ({list2[i]} > {list1[i]})")
        else:
            print("Las medias de las listas son iguales")


check_larger_num(lst1, lst2)

print("\nEJERCICIO 4.4:\n")

lst1.sort()
lst2.sort()

def print_lista_normal(lst):
    """
    Imprime una lista
    :param lst: Lista que va a ser imprimida
    :return:
    """
    for i in range(len(lst)):
        print(lst[i], end=" ")


def print_lista_reversa(lst):
    """
    Imprime una lista del revés
    :param lst: Lista que va a ser imprimida
    :return:
    """
    for i in range(len(lst)-1, -1, -1):
        print(lst[i], end=" ")


print("Lista 1, forma normal")
print_lista_normal(lst1)

print("\nLista 2, forma reversa")
print_lista_reversa(lst2)