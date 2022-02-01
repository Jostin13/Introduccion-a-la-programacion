n = int(input("Dgite un número entero"))
cn = n
if (cn < 0):
    cn = -cn
    if (cn == 0):
        #Si el número es 0, entonces n tiene 1 dígito
        #y la suma de sus cifras es 0
        sdn = 0
        nd = 1
    else:
        while (cn > 0):
                #Se acumula la suma de las cifras
                sdn = sdn + (cn %10)
                nd = nd + 1
                #Se descarta la cifra sumada
                cn = cn / 10
        print(n+" tiene " +str(nd) +" dígitos y la suma de los dígitos de" +str(n) +" es:" +str(sdn))