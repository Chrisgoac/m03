from Coche import Coche
class Camioneta(Coche):
    carga: int

    def __init__(self):
        self.carga = 2000
        Coche.__init__(self)

    def to_str(self):
        print(f"Color:  {self.color}\nRuedas: {self.ruedas}\nVelocidad: {self.velocidad}\nCilindrada: {self.cm3}\nCarga: {self.carga}")