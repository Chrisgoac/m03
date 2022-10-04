while True:
    name = input("Indica tu nombre: ")
    num = int(input("Indica el número de repeticiones: "))

    if num <= 0:
        print("El número introducido no es válido.")
        continue

    # Si se quiere separar, simplemente editar la variable name añadiendole + " " al final.
    print(name * num)
    break