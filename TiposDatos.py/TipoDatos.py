from sys import stdout
print("Programa de tpos de datos, operadores y expresiones paython")
print("Introduccion a la programacion ")
print("Jostin Gutierréz Cuenca")
print("-----")
##tipos, operadores y expresiones - int
num1= 12
num2 = 4
num3 = num1 + num2 
print("El valor de la variable num3 es: " +str(num3))

##tipos de operadores 
decimal1 = 0.5
decimal2 = 10.55
decdecimal3 = decimal1 + decimal2
print("El varlor de dec3 es: " +str(decdecimal3))
##tipos de operadores y expreciones 
print("-----")
letra1 = 'M'
letra2 = 'c'
print("Los caracteres son: "+str(letra1 + letra2)) 
##Inicializar los string
nombre ="Jostin Alejandro "
apellido ="Gutierrez Cuenca "
domicilio ="Loja "
telefono =" 0988770107 "

print("Presentar variables string")
print("Mi nombre es: "+ nombre)
print("Mi apellido es: "+ apellido)
print("Vivo en: "+ domicilio)
print("Mi numero de telefono es: "+ telefono)
print("\n")
print("Me llamo"+nombre+""+ apellido+"vivo en"+domicilio+"y mi teñefono es"+telefono+"\n")

print("***Presentar en una sola linea***")

print("me llamo,"+nombre+""+apellido+",vivo en "+domicilio+",y mi telefono es"+telefono+"\n")

print("**Presentar en una sola linea***")
    
stdout.write("me llamo  %s %s, vivo en %s y mi numero de celuilar es %s" %(nombre,apellido,domicilio,telefono))