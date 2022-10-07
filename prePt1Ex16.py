num = int(input("Escribe un número: "))
resultado = False
num_actual = 1

while num > 0:
    for i in range(2, num_actual):
        if (num_actual % i) == 0:
            resultado = True
            break
        
    if not resultado:
        num -= 1
        print(f"{num_actual}")
    num_actual += 1
    resultado = False