num = int(input("Escribe un número: "))
resultado = False

for e in range(1, num+1):
    if num > 0:
        for i in range(2, e):
            if (e % i) == 0:
                resultado = True
                break
            
    if resultado:
        print(f"El número {e} no es primo")
    else:
        print(f"El número {e} es primo")
    resultado = False
