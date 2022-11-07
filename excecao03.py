def dividir(x,y):
    try:
        resultado = x/y
        print("A resposta e: ", resultado)
    except ZeroDivisionError:
        print("Divisao por zero")

dividir(5,0)