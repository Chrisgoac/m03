from Mensaje import Mensaje

class Vehiculo:
    
    marca: str
    modelo: str
    tipo: str
    matricula: str
    gasolina: float
    velocidad: int
    mensajes = Mensaje()

    def __init__(self, marca, modelo, tipo, matricula):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.matricula = matricula
        self.gasolina = 0.0
        self.velocidad = 0
        self.mensajes = Mensaje()

    def __str__(self):
        self.mensajes.sendVerde(f"El vehiculo {self.marca} {self.modelo} del tipo {self.tipo} con matricula {self.matricula} tiene {self.gasolina} litros de gasolina y va a una velocidad de {self.velocidad}km/h.")

    def acelerar(self, value):
        if value > 0:
            if self.checkGasolinaRemain(value):
                self.velocidad += value
                self.gasolina -= value * 0.2
            else:
                self.mensajes.send_error(f"No tienes suficiente combustible para acelerar a esa velocidad. (Velocidad máxima acelerable: {self.gasolina / 0.2 - 1}km/h)")
        else:
            self.mensajes.send_error("La cantidad introducida no puede ser menor a 1.")

    def frenar(self, value):
        if value > 0:
            if self.velocidad - value > 0:
                self.velocidad -= value
            else:
                self.mensajes.send_error("El vehiculo no puede tener una velocidad negativa.")
        else:
            self.mensajes.send_error("La cantidad introducida no puede ser menor a 1.")

    def repostar(self, value):
        if value > 0:
            self.gasolina += value
        else:
            self.mensajes.send_error("La cantidad introducida no puede ser menor a 1.")

    def checkGasolinaRemain(self, value):
        if value * 0.2 < self.gasolina:
            return True
        else:
            return False

