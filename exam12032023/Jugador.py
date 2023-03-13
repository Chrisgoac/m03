from Tablero import Tablero  # Tablero es otra clase


class Jugador():
    id = ""
    nombre = ""
    num_tiradas = ""
    tablero = Tablero()
    def __init__(self):
        self.id = None
        self.nombre = None
        self.num_tiradas = None
        self.tablero = Tablero()

    def set_datos(self, id, nombre, num_tiradas):
        self.id = id
        self.nombre = nombre
        self.num_tiradas = num_tiradas

    def __str__(self):
        string = f"El jugador {self.id}, llamado {self.nombre} tiene {self.num_tiradas} disponibles."
        return string



