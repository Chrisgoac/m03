while True:
    num_piramide = int(input("Introduce el valor total de * en la pirámide: "))

    if num_piramide < 20 and num_piramide > 1:
        for i in range(1, num_piramide+1):
            print("*"*int(i))
        break
    else:
        print("El valor introducido no es válido.")