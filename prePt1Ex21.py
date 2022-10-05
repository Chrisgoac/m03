while True:
    num = int(input("Introduce un número: "))
    
    if num <= 0:
        print("Ese número no es válido.")
        continue

    for i in range(num+1):
        for a in range(i, 0, -1):
            print(a, end=" ")
        print()