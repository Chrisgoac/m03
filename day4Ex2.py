# 2.1

frase = input("Frase: ")
char = 0

for i in frase:
    char += 1
    
print(f"La frase tiene {char} carácteres.")

# 2.2 

vocales = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

nueva_frase = ""

for i in frase:
    if i in vocales:
        continue
    nueva_frase += i 
    
print(f"{frase}\n{nueva_frase}")

# 2.3

for i in range(1, len(frase)+1):
    print(frase[-i], end="")
print()

# 2.4 

nueva_frase2 = ""

for i in frase:
    if i == "o":
        nueva_frase2 += "e"
        continue
    elif i == "O":
        nueva_frase2 += "E"
        continue
    nueva_frase2 += i
print(nueva_frase2)