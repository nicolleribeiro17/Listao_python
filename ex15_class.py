# 15). Para o programa Python no arquivo ex15.py: Em uma casa, uma família decidiu dividir o valor da conta de energia entre os moradores 
# da casa. No programa eles informam o valor da conta de energia e quantos que irão pagar a conta no mês. O programa calculará quanto 
# cada um deverá contribuir com a conta de energia

class ContaEnergia:
    def __init__(self, valor, pessoas):
        self.valor = valor
        self.pessoas = pessoas

    def calculo_conta(self):
        valor_dividido = (self.valor / self.pessoas)
        return f'O valor para cada morador fica de: {valor_dividido} reais'

valor_conta = int(input('Valor da conta de energia: '))
moradores = int(input('Número de pessoas que irão pagar a conta: '))

conta = ContaEnergia(valor_conta, moradores)
print(conta.calculo_conta())