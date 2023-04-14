from Mensaje import Mensaje
from Multa import Multa
class Radar:

    marca: str
    modelo: str
    velocidad_max: int
    mensajes = Mensaje()

    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_max = velocidad
        self.mensajes = Mensaje()

    def detectar(self, vehiculo):
        return vehiculo.velocidad
    
    def comprobar(self, vehiculo):
        if self.detectar(vehiculo) > self.velocidad_max:
            return True
        else:
            return False

    def multar(self, vehiculo):
        exceso, multa = self.calcular_multa(vehiculo)
        multa = Multa(vehiculo.matricula, self.detectar(vehiculo), exceso, multa)
        return multa

    def calcular_multa(self, vehiculo):
        exceso = self.detectar(vehiculo) - self.velocidad_max
        multa = 0
        if exceso < 21:
            multa = 100
        elif exceso > 21 and exceso < 51:
            multa = 200
        else:
            multa = 400

        if vehiculo.tipo.upper() == "MOTO":
            multa = multa* 0.8

        return exceso, multa
    