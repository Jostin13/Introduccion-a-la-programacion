#Imprimir una matriz 
m=[[4, 7, 10, -1],
[9, 12, 24, 30],
[10, 8, 6, 1]]
a = ""
 
for k in range(4):
    for j in range(4):
        #print(m[k][j])
        a+=str(m[k][j])+'\t'
    print (a)
    a = ""  