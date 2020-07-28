print("¿Cuántos días tarda una rana en salir de un pozo de cierta profundidad?. Si consideramos que de día avanza una determinada cantidad de metros y por la noche retrocede una cierta cantidad de metros.\n")
metrosAltura = float(input("Ingrese la altura en metros del pozo (en metros): "))
metrosAvanza = float (input("Ingrese la cantidad de metros que avanza de día (en metros):"))
metrosCae = float(input("Ingrese la cantidad de metros que cae de noche (en metros):"))

diasXSalir = 0
dia = 1
contador = 0
while metrosAltura>contador:
    if dia == 0:
        contador = (contador - metrosCae)
        dia = 1
    if dia == 1:
        contador = (contador + metrosAvanza)
        dia = 0
    diasXSalir = diasXSalir + 1
print ("\nLa rana se demora", diasXSalir, "días en salir")