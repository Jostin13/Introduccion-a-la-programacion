aux = 0
i = 1
j = 1
n = int(input("Ingrese el tamaño del vector"))
    
#Declaracion
A = []
    
for i in range(n):
    a = [0] * n
    A.append(a)
        
for i in range( n ):
    A[i] = int( input('Ingrese los terminos del vector (%d): '%(i)))
        
#ingrese los datos del vector 
  

print("\n--Vector original--")
for i in range ( n ):           
        print("A (%d): " %(i) +str(A[i]))
            
bsc = int( input("Ingrese el numero a buscar"))
for i in range ( n ):
    if (bsc==A[i]):
        aux=aux+1
        print("Su posicion es:A["+str(i)+"]" +str(A[i]));
            
print("El numero ingresado se repite "+str(aux)+" veces en el vector")
    