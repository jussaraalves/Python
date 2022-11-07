
def soma_par(lista):
    soma = 0
    for elem in range(len(lista)):
        if(lista[elem]%2 == 0):
            soma += lista[elem]
    return soma

lista_teste = [10, 4, 3, 7, 8, 1, 9, 2]
soma = soma_par(lista_teste)
print('a soma de todos os elementos pares da lista e: {}'.format(soma))
