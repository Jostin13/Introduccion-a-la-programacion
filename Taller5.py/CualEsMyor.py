#Declaracion e inicializacion de variables
        
print("Programa para ver cuál es el número mayor de tres números\n")
        
n1 = float(input("Ingrese el primer número:\n"))
n2 = float(input("Ingrese el segundo número:\n"))
n3 = float(input("Ingrese el tercero número:\n"))

#Proceso
if (n1 > n2) and (n1 > n3):
    print("El primer número: " +str(n1), " es el mayor")
else:
    if (n2 > n1) and (n2 > n3):
        print("El segundo número: " +str(n2), " es el mayor")
    else:
        if (n3 > n1) and (n3 > n2):
            print("El tercer número: " +str(n3), " es el mayor")
        else:
            print("Los valores que ingresaste son iguales")