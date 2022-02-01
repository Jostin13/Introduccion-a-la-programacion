aux = 0
i = 1
j = 1
print("--Ordenar un vector de N elementos--\n")
n = int(input("Ingrese eltamño del vector: "))

#Declarar

A = []
for i in range(n):
    a = [0] * n
    A.append(a)

for i in range( n ):
    A[i] = int( input('Ingrese los datos de la posición A (%d): '%(i)))

#ingrese los datos del vector 
print("Ingrese los elemntos del vector")
for i in range ( n ):
    print("A (%d): " %(i) +str(A[i]))

print("\n--Vector original--")
for i in range ( n ):           
    print("A (%d): " %(i) +str(A[i]))

for i in range ( n ):
    if i < n:
        for j in range ( n ):
            if j < n :
                if(A[i]>A[j]):
                    aux=A[i]
                    A[i]=A[j]
                    A[j]=aux

print("\n--Vector ordenado--")
for i in range (n):
    if i < n:
        print("A (%d): " %(i) +str(A[i]))
