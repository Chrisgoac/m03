
""" EJERCICIO 1 (LISTAS) ---------------------------------------------------------------
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada 
asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar 
por pantalla las asignaturas que el usuario tiene que repetir.
"""

asignaturas = ["Mates", "Historia", "Lengua", "Química", "Física"]

actual = 0

while actual < len(asignaturas):
    try:
        nota = float(input(f"Nota en {asignaturas[actual]}: "))
        if nota < 0 or nota > 10:
            raise ValueError
    except ValueError:
        print("La nota debe ser un número entero o flotante. Debe ser mayor a 0 y menor o igual a 10")
        continue
    
    if nota < 5:
        actual += 1
    else:
        del asignaturas[actual]
        

print("Tienes pendiente recuperar las siguientes asignaturas: ")        
for i in asignaturas:
    print(i)

