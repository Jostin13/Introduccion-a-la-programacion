from sys import stdout
    
n = int( input( "\nIngrese el número de filas: " )) 
m = int( input( "\nIngrese el número de columnas: " )) 
#Leer datos de la matriz 
print('Ingresar datos de la matriz A:')
    
A =[]
for i in range(n):
    a = [0]*m 
    A.append(a)
    
for i in range(n):
    for j in range(m):
        A[i][j] = int( input('Ingrese los datos de la posición A (%d,%d): '%(i,j)))
            
#Presentar datos de la matriz 
print('Matriz A es:')
       
for i in range(n):
    for j in range(m):
        stdout.write(str(A[i][j])+" " )
    stdout.write("\n") 
           
    B =[]
for i in range(n):
    B = [0]*n 
    B.append(B)
        
for i in range( n ):
    for j in range(m):
        suma = suma + A[i][j]  
        
    B[i] = suma
        
    suma = 0
        
print("El Vector B es: ");
for i in range( n ):
    stdout.write(str(B[i])+" " )