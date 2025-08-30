peso = float(input("Digite seu peso (Kg): "))
altura = float(input("Digite seu altura: "))

imc = peso / (altura ** 2)
imc = round(imc, 2)

print("Seu IMC é: " + str(imc))

if imc < 18.5:
    print('Abaixo do peso.')

elif imc < 25:
    print('Abaixo do peso.')

elif imc < 30:
    print('Sobrepeso.')
    
elif imc < 35:
    print('Obesidade Grau I.')

elif imc < 40:
    print('Obesidade Grau II.')

else:
    print('Obesidade Grau III.')
    