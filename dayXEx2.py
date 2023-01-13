import random, time

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

total = 0

while total < 9:
    rand1 = random.randint(0, 2)
    rand2 = random.randint(0, 2)
    if lista[rand1][rand2] == "*":
        continue
    for i in range(3):
        for j in range(3):
            if lista[i][j] == lista[rand1][rand2] and lista[i][j] != "*":
                print("*", end=" ")
                lista[i][j] = "*"
                total += 1
            else:
                print(lista[i][j], end=" ")
        print()
    time.sleep(0.5)
    print("-----------", total)