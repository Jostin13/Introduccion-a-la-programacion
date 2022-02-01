suma = 0 
i = 1
        
#Proceso
print("---SUMA DE LOS MULTIPLOS DE 3 O 5")
while (i <=999):
    if ((i % 3 == 0) and (i % 5 == 0)):
        suma = suma + i
    
    i = i + 1
        
print("La Respuesta: " +str(suma))