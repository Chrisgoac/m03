from math import sqrt

a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))
c = int(input("Introduce el valor de c: "))

solucion_negativa = (-b-sqrt(b**2 -(4 * a * c))) / (2 * a)
solucion_positiva = (-b+sqrt(b**2 -(4 * a * c))) / (2 * a)
print(solucion_negativa)
print(solucion_positiva)