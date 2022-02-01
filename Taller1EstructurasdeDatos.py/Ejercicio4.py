aux = 0
n = int(input("Ingrese el tamaño del vector"))
    
#declaracion
A = []
par = []
impar = []
    
for i in range(n):
    a = [0] * n
    A.append(a)
    
for i in range(n):
    par= [0] * n
    par.append(par)
    
for i in range(n):
    impar = [0] * n
    impar.append(impar)
        
for i in range( n ):
    A[i] = int( input('Ingrese los terminos del vector (%d): '%(i)))
    
print("vector original")
for i in range( n ):
    print("A["+str(i)+"]="+str(A[i]))
        
for i in range( n ):
    if(A[i] %2==0):
        par[i] = A[i]
        aux = par[i]
        print("Pares [" +str(i)+"] : "+str(par[i]))
        
aux = 0
for i in range( n ):
    if (A[i] %2 !=0):
        impar[i] = A[i]
        aux = impar[i]
        print("Impares ["+str(i)+"] : "+str(impar[i]))