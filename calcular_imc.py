def calcular_imc():
    peso = eval(input('digite seu peso: '))
    print(peso)
    altura = eval(input('digite sua altura: '))
    print(altura)
    imc = peso / (altura**2)
    print (f'IMC = {imc:,.2f}')

calcular_imc()




