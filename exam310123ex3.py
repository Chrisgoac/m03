"""
-----------------------------------------------------------
EJERCICIO 3  ----------------------------------------------
-----------------------------------------------------------
(2 puntos)

Completa el ejercicio adjunto, .py
Os dejamos la información.

PARTE 1:
- Haz que funcione el código, y se muestren los 3 prints con las 3 listas

PARTE 2:
- Haz que el código principal (sin contar las listas) sea de 1 línea

"""

lst = ["Blanco", "Verde", "Amarillo", "Rojo", "Azul"]
lst2 = ["Blanco", "Negro", "Rojo", "Gris", "Naranja"]

def mostrar_lista(lst):
    for e in lst:
        print(e)

def get_coincidencias(lst, lst2):
    comparacion = []
    for i in range(len(lst)):
        if lst[i] in lst2:
            comparacion.append(lst[i])
    return comparacion


def mostrar_todo(lst, lst2):
    print("-- LST1 --")
    mostrar_lista(lst)

    print("\n-- LST2 --")
    mostrar_lista(lst2)

    lista_comparada = get_coincidencias(lst, lst2)
    print("\n-- LST COMPARADA --")
    mostrar_lista(lista_comparada)


mostrar_todo(lst, lst2)
