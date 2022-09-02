# 5) Resolva estes problemas em Python, guardando os valores e seus resultados em variáveis diferentes.

# a. Calcule a área de um quadrado cujo lado seja 2 cm.

lado = 2
area = lado * lado
print(f'A área do quadrado vale: {area}')

# b. Uma mala custa R$120,00. Esta recebeu 5% de desconto. Quanto você irá pagar por ela.

mala = 120.0
desconto = 0.05
valor = mala - (mala * desconto) 
print(f'Valor a ser pago na mala com desconto de 5%: {valor}')

## c. Um carro está viajando a uma velocidade média de 100 Km/h, o trecho de viagem será 200 Km. 
# Quantas horas irá demorar a viagem.

velocidade = 100
trechoViagem = 200
tempo = trechoViagem / velocidade
print(f'A viagem irá demorar {tempo} horas')

# d. João tem 2 pirulitos, Maria 3 pirulitos e Sofia 1 pirulito. Calcule o total de pirulitos e sua média.

pirulitosJoao = 2
pirulitosMaria = 3
pirulitosSofia = 1
soma = pirulitosJoao + pirulitosMaria + pirulitosSofia
print(f'O total de pirulitos é: {soma}')
media = (soma / 3)
media
print(f'A média de pirulitos é de: {media}')

# e. Davi tem 13 anos e sua irmã tem 7 anos. Guarde na variável eh_mais_velho a verificação se a idade de Davi 
# é maior que a idade de sua irmã.

idadeDavi = 13
idadeIrma = 7

eh_mais_velho = idadeDavi > idadeIrma
print(f'Davi é mais velho que sua irmã? {eh_mais_velho}')

