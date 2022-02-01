print("Estructuras logicas condicionales simples")
print("Programa para conversión de grados\n")
gC = float(input('Ingrese los grados centigrados: '))
    
if (gC > 0):
    gF = (9/5)*(gC+32)
    gK = gC + 273.15
    ##salida
    print("La equivalencia en grados F es: " +str(gF))
    print("La equivalencia en grados k es: " +str(gK))
else:
    print("Los grados centigrados son negativos, no se"
        + " puede realizar la conversión")