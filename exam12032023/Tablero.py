
class Tablero():
    tabl = [["A", "A", "A", "A", "B"], ["B", "B", "A", "A", "B"], ["A", "A", "A", "A", "B"], ["A", "A", "A", "A", "A"], ["A", "B", "B", "A", "A"]]

    def __init__(self) -> None:
        pass

    
    def set_estado(self, x, y):
        if self.tabl[x][y] == "A": 
            return 0
        elif self.tabl[x][y] == "B":
            return 1
        elif self.tabl[x][y] == "X" or self.tabl[x][y] == "T":
            return 2

    def set_tocado_agua(self, x, y):
        self.tabl[x][y] = "X"
    
    def set_tocado_barco(self, x, y):
        self.tabl[x][y] = "T"

    def print_tablero(self):
        for i in range(len(self.tabl)):
            for j in range(len(self.tabl[i])):
                print(self.tabl[i][j], end=" ")
            print()