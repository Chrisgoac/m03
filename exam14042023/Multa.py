class Multa:
    matricula: str
    velocidad: int
    exceso: int
    precio: int

    def __init__(self, matricula, velocidad, exceso, precio):
        self.matricula = matricula
        self.velocidad = velocidad
        self.exceso = exceso
        self.precio = precio

    def __str__(self):
        print(f"El vehiculo con matricula {self.matricula} tiene una multa de {self.precio} por conducir a una velocidad de {self.velocidad}km/h, con un exceso de {self.exceso}km/h.")
