from Database import Database
from Mensajes import Mensajes
dnis_origen = [(12345678, 'Z'), (53289712, 'T'), (32789421, 'T'), (29878941, 'D'), (87654321, 'X'), (12859721, 'F'), (89421354, 'E'), (56841315, 'N'), (22222222, 'J'), (89494131, 'G'), (92113578, 'G'), (51325761, 'L'), (55555555, 'K'), (44444444, 'A'), (51231578, 'K'), (32498796, 'A'), (47766297, 'N'), (15687912, 'A'), (47756218, 'F'), (54897215, 'X'), (40050483, 'P'), (3086736, 'K'), (31589425, 'Y'), (36879873, 'V'), (54030317, 'Y'), (54030318, 'M')]


def check_dni(num, letra):
    """
    Función que checkea si un DNI es correcto, si es así devuelve 0 y si no es correcto,
    devuelve la letra que deberia tener.
    :param num: Número del DNI que va a ser checkeado.
    :param letra: Letra del DNI que va a ser checkeada.
    """
    LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"
    if LETRAS[num % 23] == letra:
        return 0
    else: 
        return LETRAS[num % 23]
    

def setup_bbdd(dnis_origen):
    """
    Función que prepara la bbdd para que sea usada. Se crean las tablas y se insertan datos
    :return: Se devuelve el objeto de la base de datos.
    """
    bbdd = Database("data_dni.db")
    bbdd.crear_tabla("DNIs_origen_CGA")
    bbdd.set_datos("DNIs_origen_CGA", dnis_origen)
    bbdd.crear_tabla("DNIs_origen2_CGA")
    bbdd.set_datos("DNIs_origen2_CGA", dnis_origen)
    bbdd.crear_corregidos_correctos()
    return bbdd


def check_dni_cambiar_tablas(bbdd):
    """
    Función que agrega a la tabla corregido o correcto según si un DNI está bien o mal. 
    La función elimina de la tabla origen los DNIs que no estén correctamente.
    :param bbdd: Objeto de la base de datos sobre la que se está trbajando.
    """
    for i in bbdd.get_datos("DNIs_origen_CGA"):
        result = check_dni(i[0], i[1])
        if result == 0:
            Mensajes.correcto(f"El DNI {i[0]}-{i[1]} es correcto, se vuelca en la tabla DNIs_correctos.") 
            bbdd.set_dato("DNIs_correctos_CGA", i[0], i[1]) 
        else:
            bbdd.remove_dni("DNIs_origen_CGA", i[0])
            Mensajes.mensaje(f"El DNI {i[0]}-{i[1]} no es correcto, el correcto seria {i[0]}-{result} se vuelca en la tabla DNIs_corregidos.")   
            bbdd.set_dato("DNIs_corregidos_CGA", i[0], result)      
        
        
def mostrar_tabla(bbdd, tabla):
    """
    Función que imprime la tabla seleccionda en un formato específico.
    :param bbdd: Objeto de la base de datos.
    :param tabla: Nombre de la tabla que va a ser mostrada.
    """
    Mensajes.correcto(f"Tabla {tabla}:")
    Mensajes.mensaje("-----------------------------")
    for i in bbdd.get_datos(tabla):
        Mensajes.mensaje(f"DNI: {i[0]}, Letra: {i[1]}")


def check_dni_cambiar_tablas_origen2(bbdd):
    """
    Función que corrige la tabla DNIs_origen2_CGA. La función imprime el valor que ha checkeado y el valor correcto.
    :param bbdd: Objeto de la base de datos sobre la que se está trbajando.
    """
    for i in bbdd.get_datos("DNIs_origen2_CGA"):
        result = check_dni(i[0], i[1])
        if result == 0:
            Mensajes.correcto(f"Valor comprobado: {i[0]}-{i[1]} es correcto")
        else:
            Mensajes.mensaje(f"Valor comprobado: {i[0]}-{i[1]} no es correcto, el correcto seria {i[0]}-{result}.")   
            bbdd.alter_dni(i[0], result) 


bbdd = setup_bbdd(dnis_origen)
mostrar_tabla(bbdd, "DNIs_origen_CGA")
check_dni_cambiar_tablas(bbdd)
mostrar_tabla(bbdd, "DNIs_correctos_CGA")
mostrar_tabla(bbdd, "DNIs_corregidos_CGA")
bbdd.tabla_ordenada()
mostrar_tabla(bbdd, "DNIs_ordenados_CGA")
check_dni_cambiar_tablas_origen2(bbdd)
mostrar_tabla(bbdd, "DNIs_origen2_CGA")
bbdd.cerrar()
