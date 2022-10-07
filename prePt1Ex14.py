num = int(input("Escribe un número: "))
resultado = False

if num > 0:
    for i in range(2, num):
        if (num % i) == 0:
            resultado = True
            break
        
if resultado:
    print(f"El número {num} no es primo")
else:
    print(f"El número {num} es primo")