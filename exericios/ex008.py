preco_unitario = 10.00
desconto10 = 0.1
desconto20 = 0.2

quantidade = eval(input("Digite a quantidade que vai comprar: "))
if(quantidade <= 10):
    valor_final = preco_unitario * quantidade
elif(quantidade <= 20 ):
    valor_final = preco_unitario * quantidade * (1-desconto10)
else:
    valor_final = preco_unitario * quantidade * (1-desconto20)

print(f'O valor final da é: {valor_final}')