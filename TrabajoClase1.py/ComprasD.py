print("--Ingrese los datos del producto 1--")
nomProd1 = (input('Nombre: '))
precioProd1 = float(input('Precio: '))
cantProd1 = int(input('Cantidad: '))
    
print("--Ingrese los datos del producto 2--")
nomProd2 = (input('Nombre: '))
precioProd2 = float(input('Precio: '))
cantProd2 = int(input('Cantidad: '))
    
print("--Ingrese los datos del producto 3--")
nomProd3 = (input('Nombre: '))
precioProd3 = float(input('Precio: '))
cantProd3 = int(input('Cantidad: '))
    
#proceso
    
costoProd1= precioProd1 * cantProd1 
costoProd2= precioProd2 * cantProd2 
costoProd3= precioProd3 * cantProd3 
    
subTotal = (costoProd1 + costoProd2 + costoProd3)
    
if (subTotal <=10):
    desc = subTotal * 0.05
    
if ((subTotal > 10) is (subTotal <= 30)):
    desc = subTotal * 0.15
    
if (subTotal >30):
    desc = subTotal * 0.20
        
IVA = ((subTotal-desc)*0.12)
Total = ((subTotal - desc) + IVA)
    
##salida
    

print("---Producto 1--")
print("Nombre: " +str(nomProd1))
print("Precio: " +str(precioProd1))
print("Cantidad: " +str(cantProd1))
print("--------------")
print("Costo: " +str(costoProd1))


print("---Producto 2--")
print("Nombre: " +str(nomProd2))
print("Precio: " +str(precioProd2))
print("Cantidad: " +str(cantProd2))
print("--------------")
print("Costo: " +str(costoProd2))


print("---Producto 3--")
print("Nombre: " +str(nomProd3))
print("Precio: " +str(precioProd3))
print("Cantidad: " +str(cantProd3))
print("--------------")
print("Costo: " +str(costoProd3))

        
print("----------")
print("Subtotal: " +str(subTotal))
print("Descuento: " +str(desc))
print("Valor IVA" +str(IVA))
print("         -----------")
print("Total:     "+str(Total))