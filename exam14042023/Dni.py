LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"

from Mensaje import Mensaje

class Dni:
    numero: int
    letra: str
    mensajes = Mensaje()

    def __init__(self, numero, letra):
        self.numero = numero
        self.letra = letra
        self.mensajes = Mensaje()

    def validarDni(self):

        if len(str(self.numero)) == 8 or self.numero > 0:
            if self.calcularLetra() == self.letra.upper():
                self.mensajes.send_ok("El DNI del objeto es correcto.")
            else:
                self.mensajes.send_error("El DNI del objeto NO es correcto.")
        else:
            self.mensajes.send_error("El DNI del objeto NO es correcto.")


    def calcularLetra(self):
        return LETRAS[self.numero % 23]

