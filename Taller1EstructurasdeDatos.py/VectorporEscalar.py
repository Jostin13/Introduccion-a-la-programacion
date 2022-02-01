n = int(input("Ingrese el tamaño del vector"))
escalar = int(input("Ingrese el escalar"))
    
A = []
B = []
    
for i in range(n):
    A = [0] * n
    A.append(A)
        
for i in range(n):
    B = [0] * n
    B.append(B)
        
#Ingrese los elemontos del vector   
for i in range( n ):
    A[i] = int( input('Ingrese el elemento vector (%d): '%(i)))
    
#multiplicar por el escalar
for i in range( n ):
    B[i] = A[i] * escalar  
    
#presentar el vector B
for i in range( n ):
    print("B[" +str(i)+"]=" +str(B[i])); 