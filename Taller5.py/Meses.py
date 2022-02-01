
print("Calculadora básicas\n")
#Lectura de datos
print("Programa para identificar el mes a través de su número \n")
print("Escoja una opción del siguiente menú")
print("1.")
print("2.")
print("3.")
print("4.")
print("5.")
print("6.")
print("7.")
print("8.")
print("9.")
print("10.")
print("11.")
print("12.")
print("Seleccione un numero para saber el mes: ")
mes = int(input())
#Seleccion de opciones
if mes == 1:
    print(" Enero ")
elif mes == 2:
    print(" Febrero ")
elif mes == 3:
    print(" Marzo ")
elif mes == 4:
    print(" Abril ")
elif mes == 5:
    print(" Mayo ")
elif mes == 6:
    print(" Junio ")
elif mes == 7:
    print(" Julio ")
elif mes == 8:
    print(" Agosto ")
elif mes == 9:
    print(" Septiembre ")
elif mes == 10:
    print(" Octubre ")
elif mes == 11:
    print(" Noviembre ")
elif mes == 12:
    print(" Diciembre ")
else:
    if (mes > 12) and (mes < 1):
        print("Opción invalida")