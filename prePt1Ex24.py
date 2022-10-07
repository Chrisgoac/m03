antonio = [0, 5, 4, 2, 10] 
manu = [2, 5, 3, 5, 1]

media_antonio = 0
media_manu = 0

for i in antonio:
    media_antonio += i
    
for i in manu:
    media_manu += i

media_antonio = media_antonio / len(antonio)
media_manu = media_manu / len(manu)

print(f"Media de Antonio: {media_antonio}")
print(f"Media de Manu: {media_manu}\n")

for i in range(len(antonio)):
    if antonio[i] > manu[i]:
        print(f"Pt{i+1} - Antonio - {antonio[i]}")
    elif antonio[i] == manu[i]:
        print(f"Pt{i+1} - Empate - {antonio[i]}")
    else:
        print(f"Pt{i+1} - Manu - {manu[i]}")
