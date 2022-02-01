
result = 1
i = 1
    
base = (int(input("Ingrese la base \n")))
pot =  (int(input("Ingrese la potencia \n")))
    
while (i <= 3):
    result = result * base
    i = i + 1
    print("La potencia de " +str(base) +" es " +str(result))