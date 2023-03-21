from Bicicleta import Bicicleta
class Motocicleta(Bicicleta):
    velocidad: int
    cm3: int

    def __init__(self):
        self.velocidad = 300
        self.cm3 = 600
        Bicicleta.__init__(self)

    def set_velocidad(self, value):
        self.velocidad = value

    def set_cm3(self, value):
        self.cm3 = value

    def to_str(self):
        print(f"Color:  {self.color}\nRuedas: {self.ruedas}\nVelocidad: {self.velocidad}\nCilindrada: {self.cm3}\nTipo: {self.tipo}\nVelocidad: {self.velocidad}\nCilindrada: {self.cm3}")
