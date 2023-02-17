# No tenia pensado hacerlo pero queria probar más o menos el funcionamiento

f = open("Pt1UF3\\institutos.csv", "r")
# codi_centre, Denominacio_completa, Nom_naturalesa, Nom_municipi
flen = len(f.readlines())
f.seek(0)

f2 = open("Pt1UF3\\institutos_columnas.csv", "w")
for i in range(flen):
    lista = f.readline().split(";")
    f2.write(f"{lista[0]};{lista[1]};{lista[3]};{lista[16]}\n")
f.close()
f2.close()

f = open("Pt1UF3\\institutos_columnas.csv", "r")
flen = len(f.readlines())
f.seek(0)
f2 = open("Pt1UF3\\institutos_filtrados.csv", "w")

for i in range(flen):
    lista = f.readline().split(";")
    if lista[3].rstrip("\n") == "L'Hospitalet de Llobregat":
        f2.write(f"{lista[0]};{lista[1]};{lista[2]};{lista[3]}")
f.close()
f2.close()