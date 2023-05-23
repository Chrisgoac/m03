import sqlite3

class Database:
    def __init__(self, nombre_base_datos):
        self.conexion = sqlite3.connect(nombre_base_datos)
        self.cursor = self.conexion.cursor()

    def crear_tabla(self, nombre_tabla):
        """
        Función que crea una tabla dependiendo del nombre ue se especifique.
        :param nombre_tabla: Nombre de la tabla.
        """
        self.cursor.execute(f"CREATE TABLE {nombre_tabla} (dni INTEGER, letra TEXT)")
        
    def crear_corregidos_correctos(self):
        """
        Función que crea algunas tablas necesarias para el funcionamiento del programa.
        """
        self.cursor.execute(f"CREATE TABLE DNIs_correctos_CGA (dni INTEGER, letra TEXT)")
        self.cursor.execute(f"CREATE TABLE DNIs_corregidos_CGA (dni INTEGER, letra TEXT)")
        self.cursor.execute(f"CREATE TABLE DNIs_ordenados_CGA (dni INTEGER, letra TEXT)")
        
    def remove_dni(self, nombre_tabla, dni):
        """
        Función que elimina un registro de una tabla teniendo en cuenta el número de DNI
        :param dni: DNI que va a ser eliminado.
        """
        self.cursor.execute(f"DELETE FROM {nombre_tabla} WHERE dni = {dni}")

    def set_dato(self, nombre_tabla, dni, letra):
        """
        Función que inserta un DNI y una letra a la tabla deseada.
        :param nombre_tabla: Nombre de la tabla.
        :param dni: DNI que se va a insertar.
        :param letra: Letra que se va a insertar
        """
        self.cursor.execute(f"INSERT INTO {nombre_tabla} (dni, letra) VALUES ({dni}, '{letra}')")
            
    def set_datos(self, nombre_tabla, datos):
        """
        Función que inserta datos dentro de una tabla.
        :param nombre_tabla: Nombre de la tabla.
        :param datos: Conjunto de datos que se van a insertar.
        """
        for i in datos:
            self.cursor.execute(f"INSERT INTO {nombre_tabla} (dni, letra) VALUES (?, ?)", i)
            
    def tabla_ordenada(self):
        """
        Función que inserta en la tabla de DNIS ordenados los datos de ambas tablas, ordenandolos previamente.
        """
        self.cursor.execute(f"INSERT INTO DNIs_ordenados_CGA (dni, letra) SELECT DCC.dni, DCC.letra FROM DNIs_correctos_CGA DCC UNION SELECT DCG.dni, DCG.letra FROM DNIs_corregidos_CGA DCG LEFT JOIN DNIs_correctos_CGA DCC ON DCC.dni = DCG.dni WHERE DCC.dni IS NULL")

    def alter_dni(self, dni, letra):
        """
        Función que cambia la letra del DNI deseado en la tabla de la bbdd
        :param dni: Número del DNi al cual se le va a cambiar la letra
        :param letra: Letra que va a ser cambiada.
        """
        self.cursor.execute(f"UPDATE DNIs_origen2_CGA SET letra = '{letra}' WHERE dni = {dni}")

    def get_datos(self, nombre_tabla):
        """
        Función que devuelve todos los datos de la tabla deseada
        :param nombre_tabla: String del nombre de la tabla de la cual queremos obtener los datos.
        :return: Datos de la tabla
        """
        self.cursor.execute(f"SELECT * FROM {nombre_tabla}")
        return self.cursor.fetchall()

    def cerrar(self):
        """
        Función que guarda los cambios y cierra la conexión a la base de datos.
        """
        self.conexion.commit()
        self.conexion.close()