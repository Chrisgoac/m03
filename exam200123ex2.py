"""
-----------------------------------------------------------
EJERCICIO 2 ----------------------------------------------
-----------------------------------------------------------

Calcular el Máximo Común Divisor, de manera recursiva, de dos números enteros
mediante el algoritmo de Euclides, que consiste en ir restando el más pequeño al
más grande hasta que ambos sean iguales, siendo este valor el M.C.D. de los dos
números.

# Por ejemplo, si tenemos el 412 y el 184:
a) 412 228 44 44 44 44 44 36 28 20 12 8 4
b) 184 184 184 140 96 52 8 8 8 8 8 4 4

Inicialmente a) es más grande que b), por lo que restamos b) a a), quedando a) en
228, y volvemos a hacer la comprobación y el cálculo de nuevo.
Finalmente encontramos que 4 es el valor final resultante, es decir, el M.C.D. de
412 i 184 es 4.
"""


def mcd(x, y):
    """
    Función que calcula el mcd de dos números
    :param x: Primer número del cual se va a calcular el mcd
    :param y: Segundo número del cual se va a calcular el mcd
    :return: Devuelve el mcd de
    """
    if x == y:
        return x  # Solo hace falta devolver x o y, ya que en este caso, son iguales.
    if x > y:
        return mcd(x - y, y)
    else:
        return mcd(x, y - x)


print(f"El mcd de 412 y 184 es: {mcd(412, 184)}")
