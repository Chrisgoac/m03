""" EXERCICI 1_esc """
# Demana un numero qualsevol i afegeix a un fitxer.txt el següent. Demana tants com vulguis fins que l'usuari
# introdueixi el -1.

f = open("fichero.txt", "w")

while True:
    add = int(input("Introduce un num: "))
    if add == -1:
        break
    f.write(f"{add+1}\n")

f.close()


""" EXERCICI 2_esc """
# Escriu una funció que demani un nombre enter entre 1 i 10 i deseu en un fitxer amb el nom taula-n.txt
# la taula de multiplicar d'aquest nombre, done n és el número introduït.

def tabla(num):
    f = open(f"taula-{num}", "w")
    for i in range(11):
        f.write(f"{num} * {i} = {num * i}\n")
    f.close()


tabla(7)
