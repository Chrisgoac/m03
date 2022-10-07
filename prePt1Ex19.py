total = 0

while True:
    num1 = int(input("Introduce el número 1: "))
    num2 = int(input("Introduce el número 2: "))
    if num1 or num2 <= 0:
        continue
    break

for i in (range(num2)):
    if i+1 < num2:
        print(num1, end=" + ")
    else:
        print(num1, end=" = ")
    total += num1
print(total)