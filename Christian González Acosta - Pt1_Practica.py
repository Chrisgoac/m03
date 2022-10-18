"""
PT1 - NF1 - DAWBIO1 - M03
INSTRUCCIONES:
- No se permitirán prints innecesarios ni dentro de condicionales ni iteraciones, salvo que sean necesarios
- No se podrán crear nuevas listas
- No se permite el uso de metodos o funciones que no se han expuesto en clase
- Se entregará 1 archivo .py en el que se ejecutarán todos los ejercicios. Indicándose cuando se inicia
cada uno de ellos.
"""

"""
EJERCICIO 1
Elaborar un programa que realice la conversión de cm. a pulgadas. Donde 1cm = 0.39737 pulgadas.
"""
print("Inicio del ejercicio 1.\n")

cm = int(input("Índica los centímetros que deseas convertir a pulgadas: "))
print(f"{cm} son {cm*0.39737}")

"""
EJERCICIO 2
Obtener la edad de una persona en meses, si se introduce su edad en años y meses. Ejemplo: Introducimos 3 años 4 meses
debe mostrar: 40 meses.
"""
print("\nInicio del ejercicio 2.\n")
years = int(input("Índica los años: "))
months = int(input("Índica los meses: "))


print(f"Tienes {months + (years*12)} meses.")

"""
EJERCICIO 3
Los alumnos de 1º de DAWBIO realizaran un viaje a Port Aventura a final de curso, el precio de la entrada general es de 45€.
Al grupo se le aplicará un descuento dependiendo del número de alumnos:
    • Si alumnos > 50 --> 30%
    • Si alumnos entre 20  y 50 --> 20%
    • Si alumnos entre 10 y 20 € --> 10%
    • Si alumnos es <  10 € --> 0%
    • Profesor de programación --> entrada libre.

Se realizará un descuento adicional del 15% a los alumnos menores de 18 años. La cantidad de alumnos
menores del grupo se ha de indicar para obtener el precio final.

El programa mostrará el importe total a pagar para los mayores de edad, el importe a pagar para los menores de edad y 
el importe total del grupo.
"""
print("\nInicio del ejercicio 3.\n")

alumnos = int(input("Cuantos alumnos asistirán: "))
menores = int(input("Cuantos de ellos son menores: "))

alumnos_mayores = alumnos - menores

descuento = 0

if alumnos >= 10 and alumnos < 20:
        descuento = 0.90
        # descuento_menores = 0.75
elif alumnos >= 20 and alumnos < 50:
        descuento = 0.80
        # descuento_menores = 0.65
elif alumnos >= 50:
        descuento = 0.70
        # descuento_menores = 0.55
else:
        descuento = 1
        # descuento_menores = 0.85

precio_mayores = alumnos_mayores * 45 * descuento
precio_menores = menores * 45 * 0.85

total_entradas = precio_mayores + precio_menores

print(f"El total de las entradas asciende a {total_entradas} €")


"""
EJERCICIO 4
Dadas las listas:
lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0, 2,
        0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5, 3,
        5, 9, 8, 0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]
lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7, 2,
        5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9, 10, 2,
        0, 10, 7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]

4.1 - Compararemos ambas listas, mostrando por pantalla cuál de las 2 es mas larga.
4.2 - Realizaremos la media de cada una, indicando el resultado y cuál tiene la media más grande.
4.3 - Recorreremos la lista 1 y compararemos cada elemento de la lista, con el que tenga la misma posición de la otra.
 Indicando que lista posee el elemento con un valor más pequeño.
4.4 - Ordenaremos ambas listas de la misma forma y las mostraremos una de mayor a menor y la otra al revés de forma
invertida.
"""
print("\nInicio del ejercicio 4.\n")

print("Inicio del ejercicio 4.1\n")
lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0, 2,
        0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5, 3,
        5, 9, 8, 0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]
lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7, 2,
        5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9, 10, 2,
        0, 10, 7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]

lst1_lenght = 0
lst2_lenght = 0

for i in lst1:
        lst1_lenght += 1

for i in lst2:
        lst2_lenght += 1

# print(lst1_lenght)
# print(lst2_lenght)

if lst1 > lst2:
        print("La lista 1 es mayor a la lista 2.")
elif lst2 > lst1:
        print("La lista 2 es mayor a la lista 1.")
else:
        # Nunca se va a dar este caso, pero Eric, nos conocemos.
        print("Las dos listas son iguales.")

print("\nInicio del ejercicio 4.2\n")

lst1_media = 0
lst2_media = 0

for i in range(len(lst1)):
        lst1_media += lst1[i]

for i in range(len(lst2)):
        lst2_media += lst2[i]

lista1_media = lst1_media / lst1_lenght
lista2_media = lst2_media / lst2_lenght

if lista1_media > lista2_media:
        print("La media de la lista 1 es mayor a la lista 2.")
elif lista2_media > lista1_media:
        print("La media de la lista 2 es mayor a la lista 1.")
else:
        # Nunca se va a dar este caso, pero Eric, nos conocemos.
        print("Las dos listas son iguales.")

print("\nInicio del ejercicio 4.3\n")

for i in range(lst1_lenght):
        # Que no salga la excepción index out of range :(
        if i+1 > lst2_lenght:
                print(f"En la posición {i} solo la lista 1 tiene valores.") 
        elif lst1[i] > lst2[i]:
                print(f"En la posición {i} la lista 1 tiene el valor más grande.")
        elif lst2[i] > lst2[i]:
                print(f"En la posición {i} la lista 2 tiene el valor más grande.")
        else:
                print(f"En la posición {i} las dos listas tienen el mismo valor.")

print("\nInicio del ejercicio 4.4\n")

lst1_ordenada = lst1[:]
lst2_ordenada = lst2[:]

changed = True
while changed:
    changed = False
    for i in range(len(lst1_ordenada) - 1):
        if lst1_ordenada[i] > lst1_ordenada[i + 1]:
            changed = True
            lst1_ordenada[i], lst1_ordenada[i + 1] = lst1_ordenada[i + 1], lst1_ordenada[i]
changed = True

while changed:
    changed = False
    for i in range(len(lst2_ordenada) - 1):
        if lst2_ordenada[i] > lst2_ordenada[i + 1]:
            changed = True
            lst2_ordenada[i], lst2_ordenada[i + 1] = lst2_ordenada[i + 1], lst2_ordenada[i]

for i in range(len(lst1_ordenada)):
        print(lst1_ordenada[i], end=" ")

print()

for i in range(len(lst2_ordenada)-1, 0, -1):
        print(lst2_ordenada[i], end=" ")
