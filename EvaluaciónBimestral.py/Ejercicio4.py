
contraseña = 0 
intentos=1
maximo = 4
while((contraseña!=1234) and (intentos<maximo)):
    contraseña = int(input("Introduzca su contraseña: "))         
    if (intentos == 3):
        print("acceso denegado")
        intentos = intentos - maximo        
        intentos = intentos + 1
        
print("**contraseña correcta**")