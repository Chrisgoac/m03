import random

lista = []
cambiado = True
lista_resultado = []

cero_times = 0
one_times = 0
two_times = 0
three_times = 0
four_times = 0
five_times = 0
six_times = 0
seven_times = 0
eight_times = 0
nine_times = 0

for i in range(1000):
    lista.append(random.randint(0, 9))
    

while cambiado:
    cambiado = False 
    for i in range(len(lista)-1):        
        if lista[i] < lista[i+1]:
            cambiado = True
            lista[i], lista[i+1] = lista[i+1], lista[i]
            
for i in lista:
    if i == 9:
        nine_times += 1
    elif i == 8:
        eight_times += 1
    elif i == 7:
        seven_times += 1
    elif i == 6:
        six_times += 1
    elif i == 5:
        five_times += 1
    elif i == 4:
        four_times += 1
    elif i == 3:
        three_times += 1
    elif i == 2:
        two_times += 1
    elif i == 1:
        one_times += 1
    elif i == 0:
        cero_times += 1
        
        
lista_resultado.extend([cero_times, one_times, two_times, three_times, four_times, five_times, six_times, seven_times, eight_times, nine_times])

for i in range(len(lista_resultado)):
    print(f"El número {i} se repite {lista_resultado[i]} veces.")


