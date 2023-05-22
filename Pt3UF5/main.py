DICCIONARIO = {"1r.- Concurs amb complexitat.": 1, "2n.- Ordinari amb complexitat.": 2, "3r.- Concurs.": 3, "4t.- Ordinari, verbal amb complexitat i procediment social.": 4, "5è.- Verbal, verbals especials, revisió de sentència o laude ferm": 5, "5è.- Reclamació d’aliments, de cura i custòdia o règim de visites": 5, "5è.- Separació i divorci contenciós": 5, "5è.- Modificació de mesures denitives de separació o divorci": 5, "5è.- Filiació, capacitat, divisió de patrimonis o herència": 5, "5è.- Abreujat contenciós administratiu, impugnacions de sancions disciplinàries": 5, "5è.- Complement de responsabilitat civil derivada d’un procediment penal": 5, "6è.- Execució o canviari amb oposició, judici oral sumari i procediment del jurat.": 6, "7è.- Execució o canviari (demanda i la resta d’actuacions) sense oposició": 7, "7è.- Conveni regulador de divorci amb complexitat.": 7, "8è.- Mesures cautelars o provisionals amb complexitat.": 8, "8è.- Incident d’oposició a l’execució amb complexitat judici oral abreujat": 8, "8è.- Judici del jurat amb conformitat i judici oral sumari amb conformitat": 8, "9è.- Mesures cautelars o provisionals, incidents amb oposició i complexitat": 9, "9è.- Incidents concursals i judici ràpid": 9, "10è.- Declinatòria, incidents amb oposició, incident d’oposició a l’execució.": 10, "10è.- Nul·litat d’actuacions, nomenament i remoció d’àrbitres": 10, "10è.- Expedients de jurisdicció voluntària": 10, "10è.- Querella, judici oral del procediment abreviat amb conformitat": 10, "10è.- Judici sobre delictes lleus": 10, "11è.- Exequàtur, incident de liquidació d’interessos": 11, "11è.- Incident d’impugnació de taxació de costes i conveni regulador de divorci.": 11, "12è.- Demanda d’execució o de canviari, escrit de petició o d’oposició de monitori,": 12, "13è.- Sol·licitud d’ampliació de l’execució, acte de conciliació amb avinença": 13, "13è.- Incident sense oposició, mesures cautelars sense oposició": 13, "13è.- Judici ràpid amb conformitat davant del Jutjat d’Instrucció.": 13, "14è.- Recursos de reposició, revisió, reforma, queixa i súplica o similar amb complexitat": 14, "14è.- Procediment de separació i divorci de mutu acord(conveni a part) i denúncia.": 14, "15è.- Recursos de reposició, revisió, reforma, queixa i súplica o similar": 15, "15è.- Diligències preliminars civils, demanda d’execució social": 15, "15è.- Altres escrits d’al•legacions mínimament fonamentats.": 15, "16è.- Demanda de conciliació, escrit d’impugnació a l’oposició al monitori": 16, "16è.- Assistències i compareixences penals.": 16, "17è.- Compareixences de tràmit, acte de conciliació sense avinença": 17, "17è.- Petició d’aclariment o correcció d’error de resolució judicial.": 17, "18è.- Escrits de mer tràmit.": 18}

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from PIL import ImageTk,Image

def getProcedimientoKeys(dict):
    """
    Función que devuelve todas las keys del diccionario.
    :param dict: diccionario del cual se devolverán las keys.
    :return: Keys del diccionario.
    """
    return list(dict.keys())


def getProcedimientoGrado(procedimiento, dict):
    """
    Función que devuelve el grado del procedimiento que se ha seleccionado.
    :param procedimiento: String del procedimiento seleccionado.
    :param dict: diccionario de procedimientos.
    :return: Devuelve el grado del procedimiento seleccionado.
    """
    return dict[procedimiento]


def getProcedimientoTotal(procedimiento, dict, startDinero):
    """
    Función que calcular el coste total dependiendo del procedimiento y del valor de la demanda.
    :param procedimiento: Procedimiento seleccionado.
    :param dict: Diccionario con los procedimientos.
    :param startDinero: Valor de la demanda.
    :return: Devuelve el total del coste calculado del procedimiento.
    """
    grado = getProcedimientoGrado(procedimiento, dict)
    total = startDinero / 3
    for i in range(grado-1):
        total *= 0.8
        print(total)
    return total


def calcular():
    """
    Función que calcula e imprime en los diferentes campos de la GUI el coste, el coste total entre otros...
    También imprime un mensaje de error si el valor introducido no es correcto.
    """
    try:
        valor1=int(entrada1.get())
        opcion=opcion_a_elegir.get()
        if getProcedimientoGrado(opcion, DICCIONARIO) >= 15:
            valor1=18000
        total = getProcedimientoTotal(opcion, DICCIONARIO, valor1)
        area_log.insert(tk.INSERT, f"""{opcion} - {valor1} - {round(total, 2)}\n""")
        # https://stackoverflow.com/questions/56820/round-doesnt-seem-to-be-rounding-properly | Me daba 20.99999999999 (por ejemplo) cando probaba valores  
        # y quedaba muy largo en la GUI, por lo que uso este método para "redondearlo"
        #nuevo_valor = int(float(acumulado.get())) + float("{:.2f}".format(total))
        nuevo_valor = int(float(acumulado.get()) + total)
        acumulado.set(str(nuevo_valor))
        labelError.place_forget()
    except ValueError:
        labelError.place(x=30, y=60)
    

def borrar_log():
    """
    Fucnión que borra el historial de la GUI y el campo del total de los procedimientos calculados.
    """
    area_log.delete(1.0, tk.END)
    acumulado.set("0")
    entrada1.delete(0, tk.END)
    entrada1.insert(0, 18000)


# Creación de la ventana de trabajo
ventana = tk.Tk()
ventana.title("Cálculo de Honorarios")
ventana.geometry('700x190')

# Set imagen
img = ImageTk.PhotoImage(Image.open("Pt3UF5/ICAB_logo.jpg").resize((95, 95)))
lbl_img = tk.Label(ventana,image=img)
lbl_img.place(x=300, y=10)

# Etiqueta + Entrada
label1 = tk.Label(ventana, text="Cuantia del procedimiento: ")
label1.place(x=10, y=20)
entrada1 = tk.Entry(ventana)
entrada1.place(x=160, y=22)
entrada1.insert(0, 18000)
labelEuro = tk.Label(ventana, text="€")
labelEuro.place(x=280, y=20)

# Etiqueta para señalar error
labelError = tk.Label(ventana, text="El número indicado no cumple los requisitos", bg="red")

# Rellenar combobox con las opciones
opcion_a_elegir = ttk.Combobox(ventana, width=42)
opcion_a_elegir['values'] = getProcedimientoKeys(DICCIONARIO)
opcion_a_elegir.current(0)
opcion_a_elegir.place(x=10, y=100)

# Botón de calcular
button1 = ttk.Button(ventana, text="Calcular", command=calcular)
button1.place(x=300, y=110, width=100, height=30)

# Botón borrar historial
button2 = ttk.Button(ventana, text="Borrar...", command=borrar_log)
button2.place(x=300, y=140, width=100, height=30)

# Historial
area_log = scrolledtext.ScrolledText(ventana, width=38, height=10, font=("Arial", 10))
area_log.place(x=410, y=12)
area_log.insert(tk.INSERT, """Aqui irá el historial de resultados: \n""")

# Etiqueta de resultados
acumulado = tk.StringVar()
acumulado.set("0")
label_result = tk.Label(ventana, text="Resultado:")
label_vresult = tk.Label(ventana, textvariable=acumulado)
label_eresult = tk.Label(ventana, text="€")
label_result.place(x=0, y=140, width=100)
label_vresult.place(x=110, y=140, width=100)
label_eresult.place(x=220, y=140, width=80)

ventana.mainloop()