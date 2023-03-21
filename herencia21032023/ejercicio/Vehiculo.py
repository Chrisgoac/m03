class Vehiculo:
    color: str
    ruedas: int

    def __init__(self):
        self.color = "Sin especificar"
        self.ruedas = 2

    def set_color(self, value):
        self.color = value

    def to_str(self):
        print(f"Color:  {self.color}\nRuedas: {self.ruedas}")

