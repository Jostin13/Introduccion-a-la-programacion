from sys import stdout
if __name__ == '__main__':
    k = 0

    m = int( input( "\nIngrese el tamaño de la matriz: " )) 
     
    print('Ingresar datos de la matriz A:')
    
    A =[]
    for i in range(m):
        a = [0]*m 
        A.append(a)
    
    for i in range(m):
        for j in range(m):
            A[i][j] = int( input('Ingrese los datos de la posición A (%d,%d): '%(i,j)))
    
    for i in range(m):
        for j in range(m):
            if (A [i][j] == A[j][i]):
                k = k + 1
    
    if (k == m*m):
        print("La matriz es simetrica")         
    else:
        print("No es simetrica")
            