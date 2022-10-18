# Tres listas, de 500 num cada random. La media de los 100 primeros, segundos... en num asteriscos

import random

# Creamos las 3 listas random

lista1 = []
lista2 = []
lista3 = []

position = 0
total = 0
sum = 0

for i in range(500):
    lista1.append(random.randint(0, 27))
    
for i in range(500):
    lista2.append(random.randint(0, 27))
    
for i in range(500):
    lista3.append(random.randint(0, 27))
    
for i in range(5):
    for j in range(0+sum, 100+sum):
        total += lista1[j]
        
        position += 1
    for j in range(int(total/100)):
        print("*", end="")
    print()
    total = 0
    sum += 100
sum = 0

for i in range(5):
    for j in range(0+sum, 100+sum):
        total += lista2[j]
        
        position += 1
    for j in range(int(total/100)):
        print("*", end="")
    print()
    total = 0
    sum += 100
sum = 0

for i in range(5):
    for j in range(0+sum, 100+sum):
        total += lista3[j]
        
        position += 1
    for j in range(int(total/100)):
        print("*", end="")
    print()
    total = 0
    sum += 100 