from Coche import Coche
from Bicicleta import Bicicleta
from Camioneta import Camioneta
from Motocicleta import Motocicleta

list = []

def catalogar(lista, ruedas=999, contador=0):
    for i in lista:
        if ruedas == 999:
            print(f"{i.__class__}")
            i.to_str()
        else:
            if i.ruedas == ruedas:
                print(f"{i.__class__}")
                i.to_str()
                contador += 1
        print()
    print(f"Se han encontrado {contador} vehiculos de {ruedas} ruedas.")


coche = Coche()
coche.ruedas = 4
camioneta = Camioneta()
camioneta.ruedas = 4
bici = Bicicleta()
moto = Motocicleta()

list.append(coche)
list.append(camioneta)
list.append(bici)
list.append(moto)
catalogar(list, 4)

