from Mensajes import Mensajes
from math import sqrt

class Operaciones:

    operaciones_totales: int
    msgs = None

    def __init__(self, msgs):
        self.operaciones_totales = 0
        self.msgs = msgs

    def get_num_operaciones(self):
        return self.operaciones_totales

    def suma(self, x, y):
        self.add_operation()
        return x + y

    def div(self, x, y):
        self.add_operation()
        try:
            return x / y
        except Exception:
            self.msgs.error_msg()

    def potencia(self, x):
        self.add_operation()
        return x**2

    def segundo_grado(self, a, b, c):
        solucion_negativa = (-b-sqrt(b**2 -(4 * a * c))) / (2 * a)
        solucion_positiva = (-b+sqrt(b**2 -(4 * a * c))) / (2 * a)
        self.add_operation()
        return solucion_negativa, solucion_positiva
    
    def add_operation(self):
        self.operaciones_totales += 1

    