from colorama import init, Fore

init()

class ColorUtils:

    def __init__(self) -> None:
        pass

    def verde(self, msg):
        """
        Función que cambia un texto a color verde
        :param msg: El texto que va a cambiar de color
        :return: Devuelve el texto con el color cambiado
        """
        return Fore.GREEN+str(msg)

    def amarillo(self, msg):
        """
        Función que cambia un texto a color amarillo
        :param msg: El texto que va a cambiar de color
        :return: Devuelve el texto con el color cambiado
        """
        return Fore.YELLOW+str(msg)

    def rojo(self, msg):
        """
        Función que cambia un texto a color rojo
        :param msg: El texto que va a cambiar de color
        :return: Devuelve el texto con el color cambiado
        """
        return Fore.RED+str(msg)

    def reset(self, msg):
        """
        Función que cambia un texto al color por defecto
        :param msg: El texto que va a cambiar de color
        :return: Devuelve el texto con el color cambiado
        """
        return Fore.RESET+str(msg)