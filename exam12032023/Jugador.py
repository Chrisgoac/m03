from Tablero import Tablero  # Tablero es otra clase


class Jugador():
    id = ""
    nombre = ""
    num_tiradas = ""
    barcos_restantes = ""
    tablero = Tablero()
    def __init__(self):
        self.id = None
        self.nombre = None
        self.num_tiradas = None
        self.barcos_restantes = None
        self.tablero = Tablero()

    def set_datos(self, id, nombre, num_tiradas, barcos_restantes):
        """
        Función que introduce los datos en el objeto Jugador
        :param self: Se refiere a si mismo
        :param id: ID del objeto
        :param nombre: Nombre del objeto
        :param num_tiradas: Número de tiradas restantes del objeto
        :param barcos_restantes: Número de barcos_restantes del objeto
        """
        self.id = id
        self.nombre = nombre
        self.num_tiradas = num_tiradas
        self.barcos_restantes = barcos_restantes
    
    def print_tablero(self):
        """
        Función que imprime el tablero del jugador
        :param self: Se refiere a si mismo
        """
        print(f"Tablero de: {self.nombre}")
        print("-------------------")
        for i in range(len(self.tablero.tabl)):
            for j in range(len(self.tablero.tabl[i])):
                print(self.tablero.tabl[i][j], end=" ")
            print()
        print("-------------------")



