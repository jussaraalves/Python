# Exemplo de atribuicao multipla

a, b = 1, 2
print('Antes da troca')
print(f'Valor das variaveis: a={a}, b={b}')

# primeira troca
temp = a
a = b
b = temp

print('Primeira troca')
print(f'O valor das variaveis: a={a}, b={b}')

# segunda troca
a, b = b, a
print('Segunda troca')
print(f'O valor das variaveis: a={a}, b={b}')
