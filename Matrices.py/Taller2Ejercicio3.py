from sys import stdout
if __name__ == '__main__':
    i = 0 ; n=0 ; m=0 ; k=0 ; codigo = 0 ; j=0
    n = int( input( "N´umero de aspirantes que se va a seleccionar " ))
    m = int( input( "N´umero de aspirantes del proceso de selecci´on " ))
    k = int( input( "N´umero de criterios que se va a utilizar en la selecci´on " ))
    codigo =[]
    C =[]
    media=[]
    pond=[]
    p =[]
    pot=[]
    for i in range(m):
        codigo = [0]*m 
        codigo.append(codigo)

    for i in range(m):
        C = [0]*k
        C.append(C)

    for i in range(m):
        media = [0]*k 
        media.append(media)

    for i in range(k):
        p = [0]*k 
        p.append(p)

    for i in range(m):
        pot = [0]*k 
        pot.append(pot)

    """Ciclo repetitivo para que lee el vector de codigos de los aspirantes"""
    for i in range(m):
        codigo[i] = int( input("codigo " + str(i)))
        
        
    """ Ciclo repetitivo que lee los resultados de los 
        criterios (C) de cada aspirante"""        
    for i in range(m):
        for j in range(k):
            C[i][j] = int( input('Ingrese los datos de P (%d,%d): '%(i,j)))
    
    """Calculos base para la selecci´on de personal por el métodode 
        promedio simple"""
    for i in range(m):
        media[j] = 0 
        for j in range(k):
            media[j] = media[j] + C[i][j]
            
        media [i] = media[i]/k
            
    
    """Ciclo de lectura del vector fila de ponderacion"""     
    for i in range(m):
        p[i] = int( input("p" +str(i)))    
          
    
    """Calculos base para la selecci´on de personal por la media ponderada
        Ciclo que suma el vector fila de los valores ponderados"""
        
    sumap = 0
    for i in range(k):
        sumap = (int) (sumap + p[i])
        
    for i in range(m):
        pond[j] = 0 
        for j in range(k):
            pond[j] = pond[j] + C[i][j] * p[j]
            
    


