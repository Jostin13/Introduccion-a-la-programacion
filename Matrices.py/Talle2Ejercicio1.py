from sys import stdout
if __name__=='__main__':
    menor = 0
    1 - 0
    k = 0
    n= int(input( "\n Ingrese el tamaño de La matriz: "))

    print('Ingresar datos de La matriz A: ')
    A =[]
    for i in range(n):
        a = [0]*n
        A.append(a)

    for i in range (n):
        for j in range (n):
            A[i][j] = int (input('Ingrese los datos de la posición A (%d, %d): '%(i,j)))

    print('Matriz Original: ')
    for i in range (n):
            for j in range (n):
                stdout.write(str(A[i][j])+" ")
            stdout.write("\n")

    print("\n Matciz donde pares son 0")
    for i in range(n):
        A[i][0]
        for j in range (n):
            if (A[i][j]< menor):
                menor = A[i][j]
                k= 1
                l= j

