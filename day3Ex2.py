dinero_anual = int(input("Introduce el dinero que ganas anualmente: "))

impuestos = 0

if dinero_anual > 300000: 
    # Tramo 6
    tramo = 6
    impuestos = 12450 * 0.19 + 7749 * 0.24 + 14999 * 0.30 + 24599 * 0.37 + 239999 * 0.45 + (dinero_anual - 300001) * 0.47
elif dinero_anual <= 300000 and dinero_anual > 60000: 
    # Tramo 5
    tramo = 5
    impuestos = 12450 * 0.19 + 7749 * 0.24 + 14999 * 0.30 + 24599 * 0.37 + (dinero_anual - 60001) * 0.45
elif dinero_anual <= 60000 and dinero_anual > 35200: 
    # Tramo 4
    tramo = 4
    impuestos = 12450 * 0.19 + 7749 * 0.24 + 14999 * 0.30 + (dinero_anual - 35201) * 0.37
elif dinero_anual <= 35200 and dinero_anual > 20200: 
    # Tramo 3 
    tramo = 3
    impuestos = 12450 * 0.19 + 7749 * 0.24 + (dinero_anual - 20201) * 0.30
elif dinero_anual <= 20200 and dinero_anual > 12450:
    # Tramo 2
    tramo = 2
    impuestos = 12450 * 0.19 + (dinero_anual - 12450) * 0.24
elif dinero_anual < 12450 and dinero_anual >= 0:
    # Tramo 1
    tramo = 1
    impuestos = dinero_anual * 0.19
else:
    print("La cantidad introducida no es válida. Wow, no deberás pagar a hacienda :)")
    
print(f"Estás en el tramo: {tramo}, por lo que deberás pagar {impuestos}€")