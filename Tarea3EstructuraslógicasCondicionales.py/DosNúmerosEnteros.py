print("programa para identificar el divisr exacto")
num1 = float(input("Ingrese el primer número: \n" ))
num2 = float(input("Ingrese el segundo número: \n "))
    
##proceso
if (num1 > num2):
    resta = num1 - num2
    print("El resultado de la resta es: " +str(resta) + " .\n")
else:
    if (num2 > num1):
        resta= num2 - num1
        print("El resultado de la resta es: " +str(resta) + " .\n")
    
if ((num1 %resta==0 ) and (num2 %resta==0 )):
    print("La diferencia es un divisor exacto de uno de los números.")
else:
    print("La diferencia no es un divisor exacto de ningún número")
        