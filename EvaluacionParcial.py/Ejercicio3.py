print("----Programa para determinar si la diferencia de los dos numeros es"
+"multiplo de alguno de ellos----")

print("-------Programa para determinar si la diferencia de dos numeros es "
        + "múltiplo de alguno de ellos ------- \n ")
    
num1 = float(input("ingrese el primer número"))
num2 = float(input("ingrese el segundo número"))
    
#proceso
    
r1 = (num1 - num2)
    
if ((num1 % r1 == 0) and (num2 % r1 == 0)):
    print("La diferencia " +str(r1) +" es multiplo de " +str(num1) + " y " +str(num2))
else:
    if (num2 %r1 == 0):
        print("La diferencia " +str(r1) +" es multiplo de " +str(num1))
    else:
        if (num2 %r1 == 0):
            print("La difenrencia " +str(r1) +" es multiplo de " +str(num2))
        else:
            print("La difencia " +str(r1) +" no es multiplo de ninguno de los dos números")