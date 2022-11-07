
def entrada_dados():
    coeficiente = quantidade = eval(input("Digite o valor do coeficiente: "))
    return coeficiente

def calc_delta(a,b,c):
    delta = b*b-4*a*c 
    return delta

import numpy as np
def calcular_raizes(a,b,c,delta):
    if(delta<0):
        resultado='a equacao nao possui raizes nos numeros reais'
    elif(delta==0):
        x = -b/(2*a)
        resultado=f'a equacao possui apenas a raiz: {x}'
    else:
        x1= (-b-np.sqrt(delta))/(2*a)
        x2 = (-b+np.aqrt(delta))/(2*a)
        resultado = f'a equacao possui as raizes {x1}, {x2}'
    return resultado

a = entrada_dados()
b = entrada_dados()
c = entrada_dados()

delta = calc_delta(a,b,c)

resultado = calcular_raizes(a,b,c,delta)
print(resultado)