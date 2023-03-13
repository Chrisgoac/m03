
class Tablero():
    
    tabl = None

    def __init__(self):
        self.tabl = [["A", "A", "A", "A", "B"], ["B", "B", "A", "A", "B"], ["A", "A", "A", "A", "B"], ["A", "A", "A", "A", "A"], ["A", "B", "B", "A", "A"]]

    
    def set_estado(self, x, y):
        """
        Función que cambia la letra en el tablero
        :param self: Se refiere a si mismo.
        :param x: Coordenada X
        :param y: Coordenada Y
        :return: Devuelve un int dependiendo de la posición en la que haya caido la tirada.
        """
        if self.tabl[x][y] == "A":
            self.set_tocado_agua(x, y) 
            return 0
        elif self.tabl[x][y] == "B":
            self.set_tocado_barco(x, y)
            return 1
        elif self.tabl[x][y] == "X" or self.tabl[x][y] == "T":
            return 2

    def set_tocado_agua(self, x, y):
        """
        Función que setea agua tocada en el tablero
        :param self: Se refiere a si mismo.
        :param x: Coordenada X
        :param y: Coordenada Y
        """
        self.tabl[x][y] = "X"
    
    def set_tocado_barco(self, x, y):
        """
        Función que setea barco tocado en el tablero
        :param self: Se refiere a si mismo.
        :param x: Coordenada X
        :param y: Coordenada Y
        """
        self.tabl[x][y] = "T"

    