class Vehiculo:
    motor: bool
    marca: str
    ruedas: int

    def __init__(self):
        self.motor = False
        self.marca = "Sin especificar"
        self.ruedas = 2

    def encendido(self):
        self.motor = True

    def apagado(self):
        self.motor = False

    def marca(self, value):
        self.marca = value

