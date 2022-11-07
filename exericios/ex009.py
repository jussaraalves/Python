# estrategia 01
#programacao funcional
lista = [10,2,5,7,6,3]
soma = 0

for i in lista:
    if(i%2 == 0):
        soma = soma + i        
print(f'O somatorio dos elementos da lista é: {soma}')