from Dni import Dni
from Mensaje import Mensaje
mensajes = Mensaje()
dni1 = Dni(54030317, 'M')

mensajes.sendRojo(f"{dni1.numero}-{dni1.letra}")
dni1.validarDni()
mensajes.send_ok(dni1.calcularLetra())

dni2 = Dni(54030317, 'Y')

mensajes.sendRojo(f"{dni2.numero}-{dni2.letra}")
dni2.validarDni()
mensajes.send_ok(dni2.calcularLetra())
