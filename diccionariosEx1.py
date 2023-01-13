""" EJERCICIO DE REPASO DE DICCIONARIOS----------------------------------------------------------------

Mediante el uso de diccionario/s, vamos a gestionar los datos de alumnos y sus notas.
IMPORTANTE: para cada alumno, el sistema debe permitir almacenar un número indeterminado de notas.
diccionario = {"Nombre": [nota1, nota2, ...], "Nombre2": [nota1, nota2, ...], ...}

El programa va a permitir:
    - Añadir alumno: si el alumno no existe, se añadirá el nombre y la primera nota (0..10 con decimales).
      Si ya existe, mostrar mensaje de error y volver a preguntar el nombre de nuevo alumno.
    - Buscar alumno: mostrará las notas del alumno introducido por teclado. Si no existe, mostrar mensaje
      de error y volver a preguntar.
    - Añadir nota: para un alumno introducido por teclado, añadirá una nueva nota.
    - Mostrar media de notas: para un alumno introducido por teclado, mostrará la media de sus notas.
    - Borrar estudiante: borrará al alumno indicado de nuestra base de datos. Si no existe, mostrar mensaje
      de error y volver a preguntar el nombre del alumno a borrar.

NOTA: si nos hemos confundido de opción, introduciremos una "X" cuando nos pida el nombre del alumno. El sistema
volverá al menú principal. El menú se generará con lista, no un print por opción.

                                            Menú de opciones:
                                                1 - Añadir alumno
                                                2 - Buscar alumno
                                                3 - Añadir nota a alumno
                                                4 - Mostrar la media de notas de alumno
                                                5 - Borrar un alumno
                                                0 - Salir
                                            Introduce opción:
--------------------------------------------------------------------------------------------------- """

from click import pass_context


options = ["Salir", "Añadir alumno", "Buscar alumno", "Añadir nota a alumno", "Mostrar la media de notas de alumno", "Borrar un alumno", "Mostrar toda la información"]

alumnos = {}

while True:
    print("\t...:Menu:...")
    for i in range(len(options)):
        print(f"{i} - {options[i]}")
    select = int(input("\nSelecciona una opción: "))
    
    if select == 0:
        print("Has salido del programa exitosamente...")
        break
    elif select == 1:
        while True:  
            name = input("Especifica el nombre del alumno: ")          
            if name in alumnos:
                print("El alumno ya existe...")
            else:
                nota = int(input("Indica la primera nota del alumno: "))
                alumnos[name] = [nota]
                break                
        
        
    elif select == 2:
        while True:  
            name = input("Especifica el nombre del alumno: ")          
            if name in alumnos:
                print(f"Alumno {name}: ", end=" ")
                for i in range(len(alumnos[name])):
                    print(alumnos[name][i], end=" ")
                print()
                break   
            else:
                print("El alumno no existe...")
        
    elif select == 3:
        while True:  
            name = input("Especifica el nombre del alumno: ")          
            if name in alumnos:
                print(f"Agregar nota al alumno {name}")
                add_nota = int(input("Ingresa la nota que desea añadir: "))
                print(f"Se ha añadido {add_nota} a las notas del alumno {name}.")
                alumnos[name].append(add_nota)
                break 
            else:
                print("El alumno no existe...")
                
    elif select == 4:
        while True:
            name = input("Especifica el nombre del alumno: ")  
            if name in alumnos:
                media = 0
                for i in alumnos[name]:
                    media += i
                
                print(f"La media del alumno {name} es de {media/len(alumnos[name])}.")
                
                break 
            else:
                print("El alumno no existe...")
                
    elif select == 5:
        while True:
            name = input("Especifica el nombre del alumno: ")  
            if name in alumnos:
                del alumnos[name]
                print(f"Se ha borrado al alumno {name}.")
                break 
            else:
                print("El alumno no existe...")
        pass
    elif select == 6:
        for i in alumnos:
            print(f"Alumno {i} tiene las siguientes notas:", end=" ")
            for j in alumnos[i]:
                print(j, end=" ")
            print()
    else:
        pass







