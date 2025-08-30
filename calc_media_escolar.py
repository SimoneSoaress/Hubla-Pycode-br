prova_1 = float(input('Qual a nota da sua primeira prova: '))
prova_2 = float(input('Qual a nota da sua segunda prova: '))
prova_3 = float(input('Qual a nota da sua terceira prova: '))

media = (prova_1 + prova_2 + prova_3) / 3
media = round(media, 2)

print (f'Sua Média final é: {media}')

if media >= 7:
    print('Você foi APROVADO!!!')

elif media >= 5:
    print('Você está de Recuperação!')

else:
    print('Você está Reprovado.')
