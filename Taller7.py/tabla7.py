def imprimir_tabla(numero):

    LIMITE = 10

    contador = 1
    while contador <= LIMITE:
        resultado = contador * numero
        print("{} x {} = {}".format(numero, contador, resultado))

        contador = contador + 1

# Probar función
imprimir_tabla(7)