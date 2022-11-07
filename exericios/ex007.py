media = 8.5

if(media >= 7.0):
    situacao='aprovado'
elif(media >= 5.0):
    situacao='em recuperacao'
else:
    situacao='reprovado!'

print(f'O estudande está: {situacao}')
