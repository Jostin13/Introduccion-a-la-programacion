
suma = 0
i = 1
j = 1
print("--NOtas de estudiantes--\n")
n = int(input("Ingrese el numero de notas a promediar "))
    
#Declaracion
Nombre = []
Notas = []
    
for i in range(n):
    Notas = [0] * n
    Notas.append(Notas)
        
for i in range(n):
    Nombre = [0] * n
    Nombre.append(Nombre)
        
for i in range( n ):
    Nombre[i] = int( input('Ingrese el nombre (%d): '%(i)))
        
for i in range( n ):
    Notas[i] = int( input('Ingrese la nota (%d): '%(i)))
        
for i in range ( n ):
    if i < n:
        suma = suma + Notas[i]
promed = suma/(n-1)

for i in range ( n ):
    if i < n:
        print("Notas[ " +str(i) +"] =" +str(Notas[i]))
            
print("\n")
print("El promedio de Notas es: " +str(promed))
    
mayor = Notas[0]
for i in range ( n ):
    if i < n:
        if(Notas[i]<mayor):
            mayor = Notas[i]
                
    print("----" +str(mayor))   
        
print("---La nota mayor es:  " +str(mayor))
for i in range ( n ):
    if i < n:
        if(1% 2!=0):
            print("Notas["+str(i)+"] =" +str(Notas[i]))
    
print("Nombres de los estudiantes ")
    
for i in range( n ):
    Nombre[i] = str( input('Ingrese el nombre (%d): '%(i)))
        
print("\n Notas y Nombres de estudiantes")
for i in range ( n ):
    print(Nombre[i]+" tiene una nota de " +str(Notas[i]))
            