from Operaciones import Operaciones
from Mensajes import Mensajes

mensajes = Mensajes()
operaciones = Operaciones(mensajes)

mensajes.ok_msg(operaciones.suma(mensajes.get_datos("Suma-N1"), mensajes.get_datos("Suma-N2")))
mensajes.ok_msg(operaciones.div(mensajes.get_datos("Div-N1"), mensajes.get_datos("Div-N2")))

operaciones.div(8, 0)

pos, neg = operaciones.segundo_grado(mensajes.get_datos("Ecuacion-A"), mensajes.get_datos("Ecuacion-B"), mensajes.get_datos("Ecuacion-C"))
mensajes.ok_msg(f"pos: {pos}, neg: {neg}")

mensajes.warn_msg(operaciones.get_num_operaciones())
mensajes.warn_msg(mensajes.get_num_msg())