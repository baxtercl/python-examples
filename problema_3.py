print("Buscar en una secuencia de ADN ingresada por teclado el patrón A?T?, donde “?” significa que puede ser cualquiera de las cuatro letras (A, C, G, T)")
CadenaTexto = input("Ingrese una cadena de texto de no más de 100 caracteres para ADN (Ej: AATTGTAGTA)")

def buscarCadena(Cadena, Largo):
    contador = 0
    for i in range(Largo-2):
        if (Cadena[i]=='A' and Cadena[i+2]=='T'):
            contador += 1
    print("El número de apariciones es: ", contador)        
        
L = len(CadenaTexto)
buscarCadena(CadenaTexto, L)