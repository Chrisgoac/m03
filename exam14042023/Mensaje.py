from MensajesPadre import MensajesPadre
from ColorUtils import ColorUtils


class Mensaje(MensajesPadre):
    colores = ColorUtils()

    def __init__(self):
        MensajesPadre.__init__(self)
        self.colores = ColorUtils()

    def send_ok(self, msg):
        """
        Función que manda un mensaje con un formato de OK
        :param msg: Parámetro que es formateado
        """
        print(f"{self.colores.verde('OK:')} {self.colores.reset(msg)}")

    def send_error(self, msg):
        """
        Función que manda un mensaje con un formato de ERROR
        :param msg: Parámetro que es formateado
        """
        print(f"{self.colores.rojo('ERROR:')} {self.colores.reset(msg)}")

    def sendRojo(self, msg):
        """
        Función que manda un mensaje en color rojo
        :param msg: Parámetro al que se cambia el color
        """
        print(f"{self.colores.rojo(msg)}{self.colores.reset('')}")

    def sendVerde(self, msg):
        """
        Función que manda un mensaje en color verde
        :param msg: Parámetro al que se cambia el color
        """
        print(f"{self.colores.verde(msg)}{self.colores.reset('')}")
