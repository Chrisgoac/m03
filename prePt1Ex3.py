ADIV_NUM = 27

intentos_realizados = 0
notas = {0:10, 1:8, 2:6, 3:4, 4:2, 5:0}

while True:
    if intentos_realizados >= 5:
        print("No tienes más intentos.")
        break
    num = int(input("Ingresa número: "))
    if num > ADIV_NUM:
        print(f"El número es menor que {num}.")
        intentos_realizados += 1
    elif num < ADIV_NUM:
        print(f"El número es mayor que {num}.")
        intentos_realizados += 1
    else:
        print(f"Has adivinado el número usando {intentos_realizados} intentos. Tu nota ha sido de {notas[intentos_realizados]}/10")
        break