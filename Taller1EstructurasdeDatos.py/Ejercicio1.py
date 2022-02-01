 
n = 5

A = []
B = []
    
for i in range(n):
    A = [0] * n
    A.append(A)
        
for i in range(n):
    B = [0] * n
    B.append(B)
        
for i in range( n ):
    A[i] = int( input('Ingrese el vector A (%d): '%(i)))
    
for i in range( n ):
    B[i] = int( input('Ingrese el vector B (%d): '%(i)))
    
for i in range( n ):
    if i < n:
        print("A["+str(i)+"]= "+str(A[i]))
    
for i in range( n ):
    if i < n:
        print("B["+str(i)+"]= "+str(B[i]))
        
for i in range( n ):
    if (A[i]==B[i]):
        print("El vector A " +str(i) + " es = a "+str(A[i])+" y el vector B "+str(i) +" es = a "+str(B[i])+" son los mismos")
    
        
    