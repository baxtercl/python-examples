print("Determinar el monto final de ahorro, si se deposita mensualmente X cantidad de pesos en Y meses con el Z % de ganancia\n")
Ahorro = float(input("Ingrese el ahorro mensual (solo numeros enteros): "))
Interes = float(input("Ingrese el % de interés mensual: "))
Meses = int(input("Ingrese la cantidad de meses que ahorrará:"))

print("\n")
print("Mes\t Ahorro\t\t\t Total")
for i in range(1, Meses + 1): 
    if i == 1:
        Total = Ahorro
        Acum = 0
    else:
        Total = Resultado
        Acum = Resultado
    Resultado  = Ahorro + (Total * (Interes/100)) + Acum
    ResultadoFinal = round(Resultado, 2)
    print(i, "\t" , Ahorro, "+", Total,"x", (Interes/100) , "\t", ResultadoFinal)
