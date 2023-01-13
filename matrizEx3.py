menu = [[0, "Salir del menú"], [1, "Jugar"]]

lista = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]

num_x = 0

print("\t...: Menu :...")
for i in range(len(menu)):
    print(str(menu[i][0]), "-", menu[i][1])
    
print()

while True:
    select = int(input("Selecciona una opción: "))
    if select < len(menu) and select >= 0:
        break
    print("Número no válido.")
    
if select == 0:
    print("Has salido correctamente del programa.")
elif select == 1:    
        while True:
            for i in range(len(lista)):
                for j in range(len(lista[i])):
                    print(lista[i][j], end=" ")
                print()
            
            if num_x == 9:
                    print("Has ganado :)")
                    break
            
            select_frst = int(input("Selecciona cuadrante Y: "))
            select_scnd = int(input("Selecciona el cuadrante X: "))
            
            if (select_frst > len(menu) or select_frst < 0) or (select_scnd > len(menu) or select_scnd < 0):
                print("No estás dentro del rango.")
                continue
            
            if lista[select_frst][select_scnd] == "X":
                print("En esa posición ya hay X\n")
                continue
            else:
                lista[select_frst][select_scnd] = "X"
                num_x += 1
else: 
    print("Número incorrecto, aunque está validado de antes y no deberias ver nunca este mensaje...")    
    

