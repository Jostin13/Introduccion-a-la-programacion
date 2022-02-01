    
mayor = 0
n = int(input("Ingrese el tamaño del vector"))
    
#declaracion
A = []
    
for i in range(n):
    a = [0] * n
    A.append(a)
        
for i in range( n ):
    A[i] = int( input('Ingrese los terminos del vector (%d): '%(i)))
        
for i in range( n ):
    print("A["+str(i)+"]="+str(A[i]))
        
for i in range( n ):
    if (A[i] > mayor):
        mayor = A[i]
            
print("El numero mayor del vector es: "+str(mayor))