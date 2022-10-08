actual = 1

while True:
    num = int(input("Elige el tamano de la piramide: "))
    if num > 0 and num < 10:
        break
    print("Número no válido.")
    continue

while True:
    total = int(input("Elige el número de pirámides: "))
    if num > 0:
        break
    print("Número no válido.")
    continue

num += 1
for i in range(total):
    print()
    while actual < num:
        for i in range(num-actual-1):
            print(".", end="")
            
        for i in range(1, actual):
            print(i, end="")
        
        for e in range(actual, 0, -1):
            print(e, end="")
            
        for i in range(num-actual-1):
            print(".", end="")
        print()
        actual += 1
    actual = 1


