for_times = int(input("Cuantas repeticiones: "))

for i in range(for_times):
    num = int(input("Introduce valor: "))
    if num >= 0 and num % 2 == 0:
        print("El valor es par y positivo.")