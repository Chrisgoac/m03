from colorama import init, Fore

init()

class ColorUtils:

    def __init__(self) -> None:
        pass

    def verde(self, msg):
        return Fore.GREEN+str(msg)

    def amarillo(self, msg):
        return Fore.YELLOW+str(msg)

    def rojo(self, msg):
        return Fore.RED+str(msg)

    def reset(self, msg):
        return Fore.RESET+str(msg)