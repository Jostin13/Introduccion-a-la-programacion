#Declaracion e inializacion de variables
n = 0
n = float(input("Escriba la calificación del estudiante:\n"))

#Proceso
if n >= 3:
    if(n >= 4.6)&(n <= 5):
        print("Estudiante Excelente")
    else:
        if(n >= 4.1)&(n <= 4.5):
            print("El estudiante es Muy Bueno")
        else:
            if(n >= 3.6)&(n <= 4.0):
                print("El estudiante tienn una calificación Buena")
            else:
                if(n >= 3.3)&(n <= 3.5):
                    print("El estudiante tiene una calificación Aceptable")
                else:
                    if(n >= 3.0)&(n <= 3.2):
                        print("El estudiante es aprobado")
    
else:
    if(n >= 2.6)&(n <= 2.9):
        print("El estudiante tiene una calificacion y deficiente y no aprobo")
    else:
        if(n >= 2.1)&(n <= 2.5):
            print("El estudiante tiene una calificacion mala y no aprobo")
        else:
            if(n >= 0)&(n <= 2):
                print("El estudiante tiene una calificacion por mejorar y considerable, no aprobo")

if(n < 0)^(n > 5):
    print("El valor ingresado no es valido")