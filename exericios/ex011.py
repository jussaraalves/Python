lista_teste = [5, 4, 8, 3, 7]

def menor_elemento(lista):
    menor = lista[0]
    for elem in lista:
        if(elem < menor):
            menor = elem
    return menor

menor = menor_elemento(lista_teste)
print('O menor elemento da lista e: [{}]'.format(menor))