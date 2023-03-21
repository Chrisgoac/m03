from Vehiculo import Vehiculo
class Moto(Vehiculo):
    color: str
    cm3: int

    def __init__(self):
        self.color = "Sin especificar"
        self.cm3 = 49
        Vehiculo.__init__(self)

    def set_color(self, value):
        self.color = value

    def set_cm3(self, value):
        self.cm3 = value

    def to_str(self):
        print(f"Marca: {self.marca}\nEncendido: {self.motor}\nRuedas: {self.ruedas}\nColor: {self.color}\nCentímetros cúbicos: {self.cm3}")
