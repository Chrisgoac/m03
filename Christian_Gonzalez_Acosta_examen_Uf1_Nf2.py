import random as rand
"""EXAMEN NF2"""
""" 
EXAMEN NF2 - MATRICES, DICCIONARIOS Y CONTROL DE ERRORES --------------------------------------------

-----------------------------------------------------------
EJERCICIO 1  ----------------------------------------------
-----------------------------------------------------------
- Pedir al usuario su nombre y su DNI sin letra.
- Crear un diccionario con la key : nombre y el value : DNI con la letra.
- Mostrar todos los datos en forma de tabla.

                    Usuarios
                    ---------
                    Nombre --> XXXXXXXX-X

Las letras son: TRW A G M Y F P D X B N J Z S Q V H L C K E
Y las letras se relacionan del 0 al 22:
0 = T
1 = R
2 = W
etc...

"""

print("\t...:Inicio ejercicio 1:...\n")

GET_LETRA = {0:"T", 1:"R", 2:"W", 3:"A", 4:"G", 5:"M", 6:"Y", 7:"F", 8:"P", 9:"D",
 10:"X", 11:"B", 12:"N", 13:"J", 14:"Z", 15:"S", 16:"Q", 17:"V", 18:"H", 19:"L", 
 20:"C", 21:"K", 22:"E"}

usuarios = {"Eric":"34890021X", "Javi":"21899034K"}



while True:
  try:
    name = input("Introduce tu nombre: ")
    if name == "":
      raise Exception("El nombre no puede estar vacio.")
    dni = int(input("Introduce tu DNI: "))
    if len(str(dni)) != 8:
      raise ValueError
    break
  except ValueError:
    print("El DNI debe tener una longitud de 8 números, el DNI solo puede contener números enteros.")
    continue
  except Exception as e:
    print(e)


usuarios[name] = f"{dni}{GET_LETRA[dni % 23]}"

print("\n\t...:Usuarios:...")
for i in usuarios:
  print(f"{i} --> {usuarios[i]}")


"""
-----------------------------------------------------------
EJERCICIO 2: CALCULADORA DE DIVISIÓN ----------------------
-----------------------------------------------------------
- Pedir al usuario 2 números.
- While hasta que le introduzcamos 'X' en el primer valor
- Realizar la división entre ellos, gestionando todos los posibles errores y mostrando por pantalla el error.
"""

print("\n\t...:Inicio ejercicio 2:...\n")

while True:
  try:
    num1 = input("Selecciona número 1: ")
    if num1 == "X":
      print("Has salido del programa correctamente")
      break
    else:
      try:
        num1 = int(num1)
      except ValueError:
        print("El valor inroducido debe ser un numero entero")
        continue
    num2 = int(input("Selecciona número 2: "))
  except ValueError:
    print("El valor inroducido debe ser un numero entero")
    continue

  try:
    total = num1 / num2
    print(f"{num1} / {num2} es igual a {total}")
  except ZeroDivisionError:
    print("No se puede dividir entre 0.")
  


"""
-----------------------------------------------------------
EJERCICIO 3: HUNDIR LA FLOTA ------------------------------
-----------------------------------------------------------
El código va a crear un tablero de 4x4 y va a colocar 2 barcos en él. El código debe permitir, fácilmente, cambiar
la posición de los barcos antes de lanzar el programa.

# Antes de empezar a jugar:
- Creamos un tablero de 4x4 vacío ('A')
- Colocamos 2 barcos (posición con 'B'), uno de 2 celdas y otro de 3 celdas (horizontal o vertical pero que no solapen)

- En random, hacemos tiradas:
    - devolver posición de la tirada
    - devolver agua (cambiar la casilla vacía 'A' por 'X') o tocado (cambiar la casilla de barco 'B' por 'T')
    - devolver estado del tablero
    - Esperar 'ENTER' para siguiente tirada
- Al completar 6 tiradas, deberemos devolver un mensaje según si hemos conseguido hundir todos los barcos o no
"""

print("\n\t...:Inicio ejercicio 3:...\n")

# Colocación de barcos en las coordenadas que deseemos.
BARCO1 = [[0, 0], [0, 1]]
BARCO2 = [[3, 1], [3, 2], [3, 3]]

menu = ["Salir", "Jugar"]
tablero = [[" ", "0", "1", "2", "3"], ["0", "A", "A", "A", "A"], ["1", "A", "A", "A", "A"], ["2", "A", "A", "A", "A"], ["3", "A", "A", "A", "A"]]

for i in range(len(BARCO1)):
  tablero[BARCO1[i][0]+1][BARCO1[i][1]+1] = "B"

for i in range(len(BARCO2)):
  tablero[BARCO2[i][0]+1][BARCO2[i][1]+1] = "B"  

barcos = 5
tiradas = 6

print("\n\t...:Menu:...")
for i in range(len(menu)):
  print(f"{i} - {menu[i]}")

while True:
  try:
    select = int(input("Selecciona una opción: "))
    if select < 0 or select > len(menu)-1:
      raise ValueError
  except ValueError:
    print(f"La selección debe ser un número del 0 al {len(menu)-1}")
    continue

  if select == 0:
    print("Has salido correctamente.")
    break
  elif select == 1:
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
          print(tablero[i][j], end=" ")
        print()

    while barcos > 0:
      if tiradas <= 0:
        print("\nTe has quedado sin tiradas :(\n")
        break

      x = rand.randint(1, 4)
      y = rand.randint(1, 4)

      # Ha disparado a un lugar al que ya se ha disparado
      if tablero[x][y] == "X" or tablero[x][y] == "T":
        continue

      input("Presiona ENTER para continuar...")
      print(f"Se ha disparado en la posición: x = {x-1} | y = {y-1}")

      if tablero[x][y] == "A":
        # Se ha tocado agua por primera vez
        tablero[x][y] = "X"
        tiradas -= 1
        print("- Agua :(\n")
      elif tablero[x][y] == "B":
        # Se ha tocado al barco por primera vez
        tablero[x][y] = "T"
        print("- ¡Barco tocado!\n")
        barcos -= 1
        tiradas -= 1
      else:
        # Si llega aquí ya podemos asustarnos 
        continue
      for i in range(len(tablero)):
        for j in range(len(tablero[i])):
          print(tablero[i][j], end=" ")
        print()

    print("\nJuego terminado\n")
    break
  else:
    print("Esa opción no es correcta.") # No deberia llegar aquí...