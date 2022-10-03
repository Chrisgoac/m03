lista_opciones = ["Salir", "Option 1", "Option 2", "Option 3"]
num_opciones = 0
salir = False

print(len(lista_opciones))

while not salir:
    print("\tMenu")
    for i in lista_opciones:
        print(f"{num_opciones} - {i}")
        num_opciones += 1
    select = int(input("Opcion: "))
    if select == 0:
        salir = True
    elif select > 0 and select < len(lista_opciones):
        print(f"Genial, has elegido la opción: {select}")
    else:
        print("Error")
    num_opciones = 0
    
""" while not salir:
    print("\tMenu\n0 - Salir\n1 - Option 1\n")
    select = int(input("Opcion: "))
    if select == 0:
        salir = True
    elif select == 1:
        print(f"Genial, has elegido la opción: {select}")
    else:
        print("Error")
 """
