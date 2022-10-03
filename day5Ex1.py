lista = []
while True:
    num = int(input("Numero: "))
    if num == 999:
        print(f"Lista original: {lista}")
        break
    lista.append(num)

new_lista = []
for i in range(1, len(lista)+1):
    new_lista.append(lista[-i])
    
print(f"Lista inversa: {new_lista}")

max_value = 0
min_value = new_lista[0]

for i in lista:
    if i > max_value:
        max_value = i
    
for i in new_lista:
    if i < min_value:
        min_value = i
        
print(f"Mayor: {max_value}")
print(f"Menor: {min_value}")   

