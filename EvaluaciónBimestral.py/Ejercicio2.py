
i = 1
n = 20
num = 3
    
while (i <= n):
    if (num %3 == 0 ):
        print("El número " +str(num) +" es multiplo de 3")
        if (num %4 == 0 ):
            print("El número " +str(num) +" es multiplo de 4")
            if (num %20 == 0 ):
                print("El número " +str(num) +" es multiplo de 20")
                    
    num = num + 3
            
    print(i)
    i = i + 1