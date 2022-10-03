NUM_LETRAS = 23

letrasDNI = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H",
             "L", "C", "K", "E"]

dni_input = int(input("Introduce tu DNI: "))

resto = dni_input % NUM_LETRAS

print(f"Letra: {letrasDNI[resto]}, por lo que tu DNI completo es el: {dni_input}{letrasDNI[resto]}")

# Opción 2

if resto == 0:
    letra_final =  "T"
elif resto == 1:
    letra_final =  "R"
elif resto == 2:
    letra_final =  "W"
elif resto == 3:
    letra_final =  "A"
elif resto == 4:
    letra_final =  "G"
elif resto == 5:
    letra_final =  "M"
elif resto == 6:
    letra_final =  "Y"
elif resto == 7:
    letra_final = "F"
elif resto == 8:
    letra_final = "P"
elif resto == 9:
    letra_final = "D"
elif resto == 10:
    letra_final = "X"
elif resto == 11:
    letra_final = "B"
elif resto == 12:
    letra_final = "N"
elif resto == 13:
    letra_final = "J"
elif resto == 14:
    letra_final = "Z"
elif resto == 15:
    letra_final = "S"
elif resto == 16:
    letra_final = "Q"
elif resto == 17:
    letra_final = "V"
elif resto == 18:
    letra_final = "H"
elif resto == 19:
    letra_final = "L"
elif resto == 20:
    letra_final = "C"
elif resto == 21:
    letra_final = "K"
elif resto == 22:
    letra_final = "E"
else:
    print("Error, el número de DNi que has especificado no es correcto.")
    
print(f"Letra: {letra_final}, por lo que tu DNI completo es el: {dni_input}{letra_final}")

# Opcion 3
diccionaro_dni = {0:"T", 1:"R", 2:"W", 3:"A", 4:"G", 5:"M", 6:"Y", 7:"F", 8:"P", 9:"D", 10:"X", 11:"B", 12:"N", 13:"J", 14:"Z", 15:"S", 16:"Q", 17:"V", 18:"H",
             19:"L", 20:"C", 21:"K", 22:"E"}

print(f"Letra: {diccionaro_dni[resto]}, por lo que tu DNI completo es el: {dni_input}{diccionaro_dni[resto]}")

