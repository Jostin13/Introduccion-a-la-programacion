n = int(input("Ingrese el numero que desee: "))
if n > 0:
    for i in range(1,n+1):
        print("")
        for j in range(1,i+1):

            print(j,end=" ")
else:
    print("El numero ingresado no es correcto. Intente otra vez")