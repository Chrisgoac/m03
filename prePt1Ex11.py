num_list = []
imp_and_positive = []
total = 0

while True:
    num = int(input("Introduce un num: "))
    if num % 7 == 0:
        break
    num_list.append(num)
    
for i in num_list:
    if i >= 0 and i % 2 != 0:
       imp_and_positive.append(i) 
    
for i in imp_and_positive:
    total += i

print(f"La suma de los números positivos y impares es: {total}")