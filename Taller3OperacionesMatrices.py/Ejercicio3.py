from sys import stdout

if __name__ == '__main__':
    
    suma = 0
    
    fA = int( input("Ingrese el numero de filas de la matriz A: " )) 
    cA = int( input("Ingrese el numero de columnas de la matriz A:"))
    fB = int( input("Ingrese el numero de filas de la matriz B:"))
    cB = int( input("Ingrese el numero de columnas de la matriz B: "))
    
    A = [0]*fA
    B = [0]*fB
    Producto = [0]*fB
    
    for i in range(fA):
        A[i] = [0]*cA
        A.append(A)
        
    for i in range(fB):
        B [i]= [0]*cB 
        B.append(B)
        
    for i in range(fB):
        Producto [i] = [0] * cB 
        Producto.append(Producto)
    
    if  (cA==fB): 
        """Ingreso de los Datos de la Matriz A""" 
        for i in range(fA):
            for j in range(cA):
                A [i][j] = int( input('Ingrese los datos de la posición A (%d,%d): '%(i,j)))
                
        """Ingreso de los Datos de la Matriz B""" 
        for i in range(fB):
            for j in range(cB):
                B [i][j] = int( input('Ingrese los datos de la posición A (%d,%d): '%(i,j)))
        a = 0   
        for i in range(cB):
            for j in range(fB):
                for i in range(cA):
                    suma = suma + A[i][j] * B[j][a]
                    
            Producto [i][a] = suma
            suma = 0
                
        """Presentacion de Datos"""
        for i in range(fA):
            for j in range(cA):
                stdout.write(str(A[i][j])+" " )
        stdout.write("\n") 
        
        for i in range(fB):
            for j in range(cB):
                stdout.write(str(B[i][j])+" " )
        stdout.write("\n") 
        
        for i in range(fA):
            for j in range(cA):
                stdout.write(str(Producto[i][j])+" " )
        stdout.write("\n") 
          
    else:
        print("Las columnas de matriz A deben ser igual a las filas de la matriz B")  