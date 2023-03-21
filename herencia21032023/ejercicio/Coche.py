from Vehiculo import Vehiculo
class Coche(Vehiculo):
    velocidad: int
    cm3: int

    def __init__(self):
        self.velocidad = 200
        self.cm3 = 1200
        Vehiculo.__init__(self)

    def set_velocidad(self, value):
        self.velocidad = value

    def set_cm3(self, value):
        self.cm3 = value

    def to_str(self):
        print(f"Color:  {self.color}\nRuedas: {self.ruedas}\nVelocidad: {self.velocidad}\nCilindrada: {self.cm3}")
