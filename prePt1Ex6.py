# Si se quiere que sea automática la manera en la que se detectan los 100 primeros:
#     - Inicializar variable a 0, "if" para detectar que no es mayor a 100 y si es así y el residuo es cero, se imprimen en la pantalla.
for i in range(0, 201):
    if i % 2 == 0:
        print(i)