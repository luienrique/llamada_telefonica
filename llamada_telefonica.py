# programa para calcular el costo de una llamada
#input
dur_llam=int(input("dijite la duracion de la llamada:"))
# processing
if dur_llam <=3:
    print("el costo delas llamadas es 300")
else:
    costo = 300 + (dur_llam - 3) * 50

    #output
    print("el costo de las llamada es: " , costo )