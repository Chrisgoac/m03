from ColorUtils import ColorUtils

class Mensajes:

    num_mensajes: int
    color = ColorUtils()

    def __init__(self):
        self.num_mensajes = 0
        self.color = ColorUtils()

    def get_num_msg(self):
        return self.num_mensajes

    def ok_msg(self, value):
        print(self.color.verde(f"OK: {self.color.reset(value)}"))
        self.add_message()

    def warn_msg(self, value):
        print(self.color.amarillo(f"ALERTA: {self.color.reset(value)}"))
        self.add_message()

    def error_msg(self):
        print(self.color.rojo(f"Ha ocurrido un error en la aplicación.{self.color.reset('')}"))
        self.add_message()

    def get_datos(self, valor):
        v = int(input(f"Especifica el valor de {valor}: "))
        return v

    def add_message(self):
        self.num_mensajes += 1