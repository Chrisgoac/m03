num_one = int(input("Introduce el primer numero: "))
num_two = int(input("Introduce el segundo numero: "))

if num_one < num_two:
    for i in range(num_one, num_two+1):
        print(i)
else:
    for i in range(num_two, num_one+1):
        print(i)