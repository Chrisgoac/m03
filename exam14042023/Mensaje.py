from MensajesPadre import MensajesPadre
from ColorUtils import ColorUtils

class Mensaje(MensajesPadre):

    colores = ColorUtils()

    def __init__(self):
        MensajesPadre.__init__(self)
        self.colores = ColorUtils()

    def send_ok(self, msg):
        print(f"{self.colores.verde('OK:')} {self.colores.reset(msg)}")

    def send_error(self, msg):
        print(f"{self.colores.rojo('ERROR:')} {self.colores.reset(msg)}")

    def sendRojo(self, msg):
        print(f"{self.colores.rojo(msg)}{self.colores.reset('')}")

    def sendVerde(self, msg):
        print(f"{self.colores.verde(msg)}{self.colores.reset('')}")

    
        

