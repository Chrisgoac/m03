""" EJERCICIO 2 (DICCIONARIOS) ------------------------------------------------------------------
Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF,
y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono,
correo, preferente), donde preferente tendrá el valor True si se trata de un cliente
preferente. El programa debe preguntar al usuario por una opción del siguiente menú:
    (1) Añadir cliente,
    (2) Eliminar cliente,
    (3) Mostrar cliente,
    (4) Listar todos los clientes,
    (5) Listar clientes preferentes,
    (0) Terminar.
En función de la opción elegida el programa tendrá que hacer lo siguiente:

    1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
    2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
    3. Preguntar por el NIF del cliente y mostrar sus datos.
    4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
    5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
    0. Terminar el programa
"""

menu = ["Terminar", "Añadir cliente", "Eliminar cliente", "Mostrar clientes", "Listar todos los clientes", "Listar clientes preferentes"]

empleados = {}

while True:
    print("\t...:Menu:...\n")
    for i in range(len(menu)):
        print(f"{i} - {menu[i]}")
        
    print()

    option = int(input("Selecciona la opción: "))

    if option == 0:
        print("Has salido correctamente.")
        break
    elif option == 1:
        dni = input("DNI del cliente: ")
        if dni in empleados:
            print("El cliente ya está en la base de datos.")
        else:   
            name = input("Nombre del cliente: ")
            location = input("Dirección del cliente: ")
            phone = input("Teléfono del cliente: ")
            mail = input("Email del cliente: ")
            preferente = input("El cliente es preferente? (S/N): ")
            
            empleados[dni] = [name, location, phone, mail, preferente=="S"]
            print(empleados)
    elif option == 2:
        del_user = input("DNI del usuario a eliminar: ")
        if del_user in empleados:
            del empleados[del_user]
        else:
            print("Ese empelado no está en nuestra base de datos.")
    elif option == 3:
        select_cliente = input("DNI del cliente que deseas mostrar: ")
        if select_cliente in empleados:
            print(empleados[select_cliente])            
        else:
            print("Ese cliente no está en la base de datos.")
        
    elif option == 4:
        print("Option 4")
        print(empleados)
        for i in empleados:
            print("F")
            print(f"Cliente: {i}")
        
        
    elif option == 5:
        for i in empleados:
            print(i)