#10) Crie o seguinte programa Python no arquivo lista03_02.py:
# Colete o nome da pessoa, a cidade de nascimento dela, e o ano em que ela nasceu. 
# Depois você irá mostrar os dados coletados em linhas diferentes.  E também, deverá informar quantos 
# anos a pessoa terá no ano 2030.

nome = input('Digite seu nome:')
dataNascimento = int(input('Ano de nascimento:'))
cidadeNatal = input('Cidade Natal: ')

idadeFutura = 2030 - dataNascimento

print(f'Nome: {nome}')
print(f'Ano de nascimento: {dataNascimento}')
print(f'Cidade Natal: {cidadeNatal}')
print(f'Em 2030 a pessoa terá: {idadeFutura} anos')