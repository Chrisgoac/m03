lst = [[1,2,4,5,6,7,8,9], [6,7,8,9], [10,11,12,13]]

for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end=" ")
    print()
    
lst2 = [[(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)]]

print()

for i in range(len(lst2)):
    for j in range(len(lst2[i])):
        for e in range(len(lst2[i][j])):
            print(lst2[i][j][e], end=" ")
    print()