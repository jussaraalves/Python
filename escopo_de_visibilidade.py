def multiplicador(numero):
    a = 2  # esta variável tem escopo local
    print(f"Dentro da funcao, a variavel vale: {a}")
    return a * numero


a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"Fora da funcao, a variavel a vale: {a}")
