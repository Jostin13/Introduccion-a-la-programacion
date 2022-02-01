from sys import stdout
if __name__ == '__main__':
    
    aux = 0
    
    m = int( input("Ingrese el tamaño de la matriz "))
    
    A = [0]*m
    
    for i in range(m):
        A[i] = [0]*m
        A.append(A)
        
    for i in range(m):
        for j in range(m):
            A[i][j] = int( input('Ingrese los datos de la posición A (%d,%d): '%(i,j)))
    
    for i in range(m):
        for j in range(m):       
            A[i][j] = 0
            if (j == m - 1):
                aux = aux + 1
                
        if (i == m - 2):
                i = m
                
    for i in range(m):
        for j in range(m):       
            stdout.write(str(A[i][j])+" " )
        stdout.write("\n") 