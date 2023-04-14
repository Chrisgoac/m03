from Vehiculo import Vehiculo
from Radar import Radar
moto = Vehiculo("Kawasaki", "Ninja", "Moto", "1528DWP")
coche = Vehiculo("Seat", "León", "Coche", "1618DWP")

radar1 = Radar("RadaresExpress", "ExpressVolt3000", 70)

coche.repostar(200)
coche.acelerar(170)
coche.frenar(-10)
coche.frenar(19)

moto.repostar(200)
moto.acelerar(142)
moto.frenar(2)

coche.__str__()
moto.__str__()

coche.mensajes.sendRojo(f"Coche multable: {radar1.comprobar(coche)}")
moto.mensajes.sendRojo(f"Moto multable: {radar1.comprobar(moto)}")

multa_coche = radar1.multar(coche)
multa_moto = radar1.multar(moto)
multa_coche.__str__()
multa_moto.__str__()

moto.mensajes.ok_msg()

moto.frenar(70)
moto.mensajes.sendVerde(f"Moto multable: {radar1.comprobar(moto)}")



