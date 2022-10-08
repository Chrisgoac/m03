while True:
    num = int(input("Introduce un número: "))
    if num > 0:
        break
    print("Ese número no es válido.")
    continue

total = num / 4

print(f"Del 1 al {num} hay {int(total)} años bisisestos.")