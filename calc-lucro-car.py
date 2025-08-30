valor_pago = float(input('Qual foi o valor pago no carro: '))
valor_investido = float(input('Qual valor investido com reformas no carro: '))
valor_venda = float(input('Qual foi o valor de venda do carro: '))

custo_total = valor_pago + valor_investido

lucro = valor_venda - custo_total

print(f'O Custo total com o veiculo foi de R${custo_total:.3f}k')
print(f'O LUCRO obtido com o veiculo é de R${lucro:.3f}k')

if lucro > 0:
    print('Resultado: LUCRO na venda!!!')

elif lucro < 0:
    print('Resultado: PREJUIZO na venda!')

else:
    print('Resultado: Nessa venda você não teve nem lucro e nem prejuizo, ficou tudo no zero a zero!!')

