while True:
    num = int(input("Introduce un número: "))
    
    if num <= 0:
        print("Ese número no es válido.")
        continue

    for i in range(num, 0, -1):
        for a in range(1, i+1):
            print(a, end=" ")
        print()