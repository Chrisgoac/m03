NUM = 5
actual = NUM
while actual > 0:
    for i in range(NUM-actual):
        print(".", end="")
        
    for i in range(1, actual):
        print(i, end="")
    
    for e in range(actual, 0, -1):
        print(e, end="")
        
    for i in range(NUM-actual):
        print(".", end="")
    print()
    actual -= 1


