hora = 20
minutos = 21
segundos = 17

# É importante observar que a quantidade de chaves precisa ser igual à quantidade de variáveis passadas como parâmetros no método format().
# print('{} : {} : {}'.format(hora, minutos, segundos))

print(f'{hora} : {minutos} : {segundos}')
print('{:8.5}'.format(10/3))
# Ao usar {:8.5}, estamos determinando que a impressão será com 8 espaços, mas apenas 5 serão utilizados.
