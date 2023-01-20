# He puesto que el intento empiece por el 1 ya que si no, hacia 4 intentos antes de perder.

def jugar(intento=1):
    respuesta = input("¿De qué color es una naranja? ")
    if respuesta != "naranja":
        if intento < 3:
            print("\nFallaste! Inténtalo de nuevo")
            intento += 1
            jugar(intento)
        else:
            print("\nPerdiste!")
    else:
        print("\nGanaste!")


jugar()
