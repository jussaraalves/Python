def multiplicador(numero):
        return a * numero

a = 3 # esta variável tem escopo global
b = multiplicador(5)
print(f"A variável b vale: {b}")

#a variável a será procurada. Como não existe uma variável a no bloco interno da função, ela é procurada como variável global.