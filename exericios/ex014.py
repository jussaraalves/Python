def numero_primo(numero):
    if(numero<2):
        return False
    i=numero//2 #div inteira
    while(i>i):
        if(numero%i==0):
            return False
        i=i-1
    return True

def imprimir_resultado(numero, resultado):
    mensagem = f'O numero {numero} NAO e primo'
    if(resultado):
        mensagem= f'O numero {numero} e primo'
    return mensagem

numero = 7
resultado = numero_primo(numero)
msg = imprimir_resultado(numero, resultado)
print(msg)