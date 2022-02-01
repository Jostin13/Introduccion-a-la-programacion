    
aprob = 0
reprob = 0
alum = 0
n = (int(input("Ingrese cuantos alumnos va a calificar: ")))
    
nota = (int(input("Ingrese la nota del estudiante: ")))
while (alum <= n):
    if(nota < 7):
        reprob = reprob + 1
    else:
        aprob = aprob + 1
            
    alum = alum + 1
        
    print("La cantidad de alumnos que aprobaron fueron: "+str(aprob))
    print("La cantidad de alumnos que reprobaron fueron: "+str(reprob))