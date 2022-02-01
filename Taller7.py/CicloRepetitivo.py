cont = 1; limite = 0; suma = 0
        
#Pedir que se ingrese el limite de los numeros
limite = int(input("Ingrese la cantidad de numeros que quiere que se imprima: "))

#Iniciamos el ciclo repetitivo While
while cont <= limite:
    print(cont)
    suma = suma + cont
    cont = cont + 1
print("\nLa suma de los números es: ", suma)
   
i = 1
suma = 0
    
n = int(input("Ingrese el número de ciclo \n"))

##proceso
while (i < n):
    print(i)
    i = i + 1
    suma = suma + i
        
print("i es: " +str(i))   
print("i es: " +str(suma))
    
suma = 0
i = n
while (i >= 1):
    print("suma " +str(suma))
    suma = suma + 1
    print(i)
    i = i - 1           
print("i es: " +str(i))
print("i es: " +str(suma))