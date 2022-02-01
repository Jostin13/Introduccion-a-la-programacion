print("Ingrese todos sus datos con números \n")
añonaci = float(input("Ingrese año de nacimiento: \n"))
mesnaci = float(input("Ingrese mes de nacimiento: \n"))
dianaci = float(input("Ingrese día de nacimiento: \n"))
    
añoactu = float(input("Ingrese el año actual: \n"))
mesactu = float(input("Ingrese el mes actual: \n"))
diactu = float(input("Ingrese el día actual: \n"))
    
##proceso
if(((mesnaci > mesactu) and (mesactu <= 12) and (mesnaci <= 12))):
    añop = (añoactu - añonaci)-1
else:
    añop = añoactu - añonaci
    
if (mesnaci < mesactu):
    mesp = (mesactu - mesnaci)
else:
    mesp = (mesnaci - mesactu)
    
if (dianaci > diactu):
    mesp = mesp + 1
    diap = dianaci + diactu
else:
    diap = diactu - dianaci 
    
if (mesp > 12):
    añop = añop + 1
    
if(diap > 30):
    diap = mesp + 1
        
##salida
print("la persona tiene "+str(añop) + " años, " +str(mesp) +" meses y " +str(diap) +" días." )
    
           
           