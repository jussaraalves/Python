#estrategia 02

lista = [10, 2, 3, 5, 8, 11]
soma = 0
# Len () é uma função integrada ao Python que é utilizada para obter o número de itens em um determinado objeto, string, array, listas, entre outros.
for i in range(len(lista)):
    if(lista[i]%2 == 0):
        soma+=lista[i]
print('O somatorio dos elementos da lista e: {}'.format(soma))