def potencia(numero, elevado):
    if elevado == 0:
        return 1
    elif numero == 0:
        return 0
    elif elevado == 1:
        return numero
    else:
        return numero * potencia(numero, elevado-1)


print(potencia(2, 8))
print(potencia(0, 5))
print(potencia(5, 0))
print(potencia(5, 1))
