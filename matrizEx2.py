menu = [[1, "Salir del menú"], [2, "Opción 2"], [3, "Opción 3"], [4, "Opción 4"]]

""" add_num = int(input("Añadir el número de la lista: "))
add_option = input("Añadir el texto a la lista: ")

menu.append([add_num, add_option]) """

""" for i in range(len(menu)):
    print(str(menu[i][0]), "-", menu[i][1])
    
print() """

while True:
    
    add_option = input("Añadir el texto a la lista: ")
    
    if add_option == "pepe":
        break
    
    menu.append([len(menu)+1, add_option])

for i in range(len(menu)):
    for j in range(len(menu[i])):
        print(menu[i][j], end=" - ")
    print()