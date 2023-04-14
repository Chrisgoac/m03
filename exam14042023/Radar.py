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
        """
        Función que devuelve la velocidad de un vehículo
        :param vehiculo: Vehiculo del cual va a ser la velocidad devuelta
        :return: Devuelve la velocidad del vehiculo
        """
        return vehiculo.velocidad
    
    def comprobar(self, vehiculo):
        """
        Función que comprueba si un vehiculo es multable
        :param vehiculo:
        :return: Booleano de si el vehiculo es multable o no (se pasa de la velocidad máxima del radar)
        """
        if self.detectar(vehiculo) > self.velocidad_max:
            return True
        else:
            return False

    def multar(self, vehiculo):
        """
        Función que multa a un vehiculo
        :param vehiculo: Parámetro del vehiculo que va a ser multado
        :return: Devuelve la multa que se ha creado
        """
        exceso, multa = self.calcular_multa(vehiculo)
        multa = Multa(vehiculo.matricula, self.detectar(vehiculo), exceso, multa)
        return multa

    def calcular_multa(self, vehiculo):
        """
        Función que calcula cuanto se debe pagar de multa
        :param vehiculo: Vehiculo al cual se va a calcular la multa
        :return: Devuelve el exceso de velocidad y el precio de la multa que se tendrá que pagar.
        """
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
    