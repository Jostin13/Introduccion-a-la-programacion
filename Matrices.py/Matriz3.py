from sys import stdout

if __name__ == '__main__':
    n = int( input( "\nIngrese el número de filas: " )) 
    
#Leer datos de la matriz 
print('Ingresar datos de la matriz A:')
    
A =[]
for i in range(n):
    a = [0]*n 
    A.append(a)
    
for i in range(n):
    for j in range(n):
        A[i][j] = int( input('Ingrese los datos de la posición A (%d,%d): '%(i,j)))
            
#Presentar datos de la matriz 
print('Matriz Original:')
       
for i in range(n):
    for j in range(n):
        stdout.write(str(A[i][j])+" " )
    stdout.write("\n") 
           
print("\n Cambiar con 0 la diagonal principal")
for i in range(n):
    for j in range(n):
        if (i == j):
            A[i][j] = 0
                
for i in range(n):
    for j in range(n):
        stdout.write(str(A[i][j])+" " )
    stdout.write("\n")
        
print("\n Cambiar con 1 la diagonal secundaria")
for i in range(n):
    for j in range(n):
        if ((i + j) == (n-1)):
            A[i][j] = 1
                
for i in range(n):
    for j in range(n):
        stdout.write(str(A[i][j])+" " )
    stdout.write("\n") 
        
print("\n Cambiar Esquinas")
A[0][0] = 99
A[0][n-1] = 99
A[n-1][0] = 99
A[n-1][n-1] = 99
for i in range(n):
    for j in range(n):
        stdout.write(str(A[i][j])+" " )
    stdout.write("\n") 
       
    