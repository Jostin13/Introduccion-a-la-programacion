from sys import stdout
if __name__ == '__main__':
    
    n = int( input( "Ingrese las columnas de la Matriz A: " )) 
    m = int( input("Ingrese las filas de la Matriz A: "))
    
    A = [0]*m
    B = [0]*m
    
    
    for i in range(m):
        A[i] = [0]*n
        A.append(A)
        
    for i in range(m):
        B [i]= [0]*n 
        B.append(B)
        
    for i in range(m):
        for j in range(n):
            A[i][j] = int( input('Ingrese los datos de la posición A (%d,%d): '%(i,j)))
            
    for i in range(n):
        for j in range(m):
            B[i][j] = A[j][i] 
            
    for i in range(n):
        for j in range(m):
            stdout.write(str(A[i][j])+" " )
        stdout.write("\n") 
        
    for i in range(n):
        for j in range(m):
            stdout.write(str(B[i][j]) +" ")
        stdout.write("\n") 
    
    