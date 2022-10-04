years_old = int(input("Introduce los años que cumples/has cumplido este año: "))
year = int(input("Introduce el año actual: "))

NACIMIENTO = year - years_old

print(f"Naciste en {year}")
for i in range(1, years_old+1):
    if i == years_old:
        print(f"Ahora tienes {years_old}.")
    else:  
        print(f"En {NACIMIENTO+i} tenias {i} años.")


