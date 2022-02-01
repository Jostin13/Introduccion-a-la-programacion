from sys import stdout

if __name__ == '__main__':
    suma = 0
    
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
           
print("\n Matriz donde pares son 0")
for i in range(n):
    for j in range(n):
        if ((A[i][j]) %2 == 0 ):
            A[i][j] = 0
                
for i in range(n):
    for j in range(n):
        stdout.write(str(A[i][j])+" " )
    stdout.write("\n")
        
print("\n Matriz donde se remplaza i o j")
for i in range(n):
    for j in range(n):
        if (i == n-1 ):  
            if (j == n-1):
                A[i][j] = 1
                
for i in range(n):
    for j in range(n):
        stdout.write(str(A[i][j])+" " )
    stdout.write("\n")