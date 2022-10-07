CAP_INICIAL = 1000
INCREMENTO = 0.10
TOTAL_YEARS = 5

cap_actual = CAP_INICIAL

while True:
    print("\t**************MENU**************")
    print("1 - Tabla interés de un capital\n2 - Salir")
    select = int(input("Selecciona la opción: "))

    if select == 1:
        # TODO Preguntar tabla
        print("AÑO    %r  I          CA")
        for i in range(1, TOTAL_YEARS+1):
            print(f"{i}      {int(INCREMENTO*100)}   {cap_actual*INCREMENTO}    {cap_actual+(cap_actual*INCREMENTO)}")
            cap_actual += cap_actual*INCREMENTO
        print("")
    elif select == 2:
        break
    else:
        print("Esa opción no es correcta.")

    