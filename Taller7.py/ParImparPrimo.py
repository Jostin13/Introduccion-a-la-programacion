n = int(input("Ingrese el límite de números a verificar"))
    
for i in range(0,n,1):
    num = int(input("Ingrese un número"))
##verificar
        
if (num %2 == 0):
    print("El numero " +str(num) +"es Par \n")
else:
    print("El numer " +str(num) +"es Impar \n")
            
##verificar si un numero es primo
divisor = 0
j = 1
while (j <= n):
    if (num %j == 0):
        divisor = divisor +1
        j = j +1
        
if divisor == 2:
    print("El numero " +str(num) +"es Primo")
else:
    print("El numero " +str(num) +"no es Primo")
    divisor = 0