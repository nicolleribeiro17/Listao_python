# 15). Para o programa Python no arquivo ex15.py:
#Em uma casa, uma família decidiu dividir o valor da conta de energia entre os moradores da casa. 
# No programa eles informam o valor da conta de energia e quantos que irão pagar a conta no mês. 
# O programa calculará quanto cada um deverá contribuir com a conta de energia.

pessoas = int(input('Quantas pessoas residem na casa: '))
valorConta = float(input('Digite o valor da conta de energia:'))

divisao = valorConta / pessoas
type(divisao)

#divisao
print(f'O valor que cada pessoa irá pagar é de: {divisao}')