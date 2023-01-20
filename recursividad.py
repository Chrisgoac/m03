# Ejercicio 1
MENU = ["Salir", "Option 1", "Option 2"]


def mostrar_menu(menu):
    """
    Método que te muestra el menú con su indice en pantalla.
    :param menu: Lista que hará de menu
    :return: 
    """
    for i in range(len(menu)):
        print(f"{i} - {menu[i]}")

    select = int(input("Opción del menú deseada: "))

    return select


def otro_metodo():
    selection = mostrar_menu(MENU)
    if selection == 0:
        print("Has salido del programa.")
    elif selection == 1:
        print("La opción 1")
    elif selection == 2:
        print("La opción 2")
    else:
        print("La opción no está dentro de las opciones disponibles.")
        otro_metodo()


otro_metodo()
