suma = 0
num = 1
den = 7
i = 1
n = int(input("Ingrese el límite: "))
        
#Proceso
    
while (i <= n):
    if(num <= 1):
        num = num +1
        if(num >= 2):
            num = num -1
        term = num/den
        print("El termino " +str(i) +"es: " +str(num) +"/" +str(den));
        suma = suma + term
          
        den = den + 3
        i = i + 1
    print("la suma es: " +str(suma))