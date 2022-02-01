print("Calculadora básicas\n")
#Lectura de datos
n = float(input("Ingrese el número a verificar: "))
    
#Menú de opciones
print("Seleccione la operacion del siguiente menu")
print("1. Par impar")
print("2. Positivo o negativo")
print("3. Multiplo de 3")
print("4. numero primo")
Opc = int(input())
    
#Seleccion de opciones
if Opc == 1:
    if(n % 2 == 0):
        print("par " +str(n))
    else:
        print("impar " +str(n))
    
elif Opc == 2:
    if(n == 0):
        print("El 0 es numero neutral, digite otro numero ecepto cero")
    else:
        if(n > 0):
            print("El número " +n +" es positivo.\n" )
        else:
            if (n < 0): 
                print("El número " +n +" es negativo.\n" )
elif Opc == 3:
    if(n % 3 == 0):
        print("multiplo de 3 " +str(n))
    else:
        print("el número " +str(n) +" no es multiplo de 3")
elif Opc == 4:
    if (n == 2):
        print("El numero " +str(n) +" es Primo")      
    else:
        print("El numero " +str(n) +" no es Primo")