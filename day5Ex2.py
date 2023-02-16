lista = [0,1,3,7,9,4,5,5,5,6,9,10,10,0,3,4,5,6]

cambiado = True

while cambiado:
    print("Whilee")
    cambiado = False 
    for i in range(len(lista)-1):        
        if lista[i] < lista[i+1]:
            cambiado = True
            lista[i], lista[i+1] = lista[i+1], lista[i]
print(lista)
            


