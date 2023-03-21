import exAlumno28022023 as lib
import random as rand

IDS = [1, 2, 3, 4]
NOMBRES = ["Esteban", "Carlos", "Rodolfo", "Alberto"]
EDADES = [19, 27, 29, 32]
ALTURAS = [162, 188, 177, 167]
MODULOS = [["Web", "BBDD"], ["Web", "BBDD"], ["BBDD", "Programación"], ["Programación", "Web"]]

def new_random_alumno(id, nombre, edad, altura, modulo):
    alum = lib.Alumno()
    alum.load_data(id[rand.randrange(1, 4)], nombre[rand.randrange(1, 4)], edad[rand.randrange(1, 4)], altura[rand.randrange(1, 4)], modulo[rand.randrange(1, 4)])
    alum.load_data(1, "Eric", 2, 3, ["a", "b"])
    return alum

alum2 = lib.Alumno()
print(alum2.get_id())
alumno = new_random_alumno(IDS, NOMBRES, EDADES, ALTURAS, MODULOS)
print(alumno.to_string())



