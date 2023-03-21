from Vehiculo import Vehiculo
class Bicicleta(Vehiculo):
    tipo: str

    def __init__(self):
        self.tipo = "Urbana"
        Vehiculo.__init__(self)

    def set_tipo(self, value):
        self.tipo = value

    def to_str(self):
        print(f"Color:  {self.color}\nRuedas: {self.ruedas}\nTipo: {self.tipo}")
