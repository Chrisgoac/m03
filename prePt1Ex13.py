# Sí, Eric. Sé que el mes puede ser mayor que 12, el día mayor que 31...

total = 0

for i in range(10):
    day = int(input("Indica tu día de nacimiento: "))
    month = int(input("Indica tu mes de nacimiento: "))
    year = int(input("Indica tu año de nacimiento: "))
    print("-----------------------------")
    
    if year >= 1980 and year <= 2000:
        total += 1
        
print(f"El total de nacidos ente el 01-01-1980 y el 31-12-2000 es de {total} personas.")