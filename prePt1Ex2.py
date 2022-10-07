lista = []
while len(lista) < 4:
    num = int(input("Escribe un número mútliplo de 3: "))
    if num % 3 == 0:
        lista.append(num)
    else:
        print("Ese número no es múltiplo de 3.")
        
for i in range(len(lista)):
    print(lista[i]**2)