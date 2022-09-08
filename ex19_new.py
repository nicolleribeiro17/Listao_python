#19).Um vendedor ganha uma comissão de uma venda da seguinte forma: Se a venda for ...
# ● menor que R$1000,00, o vendedor não ganha nenhuma comissão;
# ● entre R$1.000,00 e R$5.000,00, o vendedor ganha uma comissão de 10% davenda;
# ● entre R$5.000,00 e R$10.000,00, a comissão será de 20% da venda;
# ● entre R$10.000,00 e R$50.000,00 a comissão será de 25% da venda;
# ● acima de R$50.000,00 a comissão será de 30% da venda.
# Faça um programa que informe o valor da comissão do vendedor para uma venda.

from venda import Venda

valor_venda = float(input('Digite o valor de sua venda: '))
vendedor1 = input('Digite seu nome: ')

comissao_venda = Venda(valor_venda, vendedor1)
print(comissao_venda.calcula_comissao())
