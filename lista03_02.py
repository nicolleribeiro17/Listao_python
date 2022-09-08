#10) Crie o seguinte programa Python no arquivo lista03_02.py: Colete o nome da pessoa, a cidade de nascimento dela, e o ano em que ela nasceu. 
# Depois você irá mostrar os dados coletados em linhas diferentes. E também, deverá informar quantos anos a pessoa terá no ano 2030.

class Pessoa():
    def __init__(self, nome, cidade, ano):
        self.nome = nome
        self.cidade = cidade
        self.ano = ano

    def get_people(self):
        dados = f'Nome: {self.nome} \nCidade: {self.cidade} \nAno que nasceu: {self.ano}'
        return(dados)

    def set_people(self):
        idade_futura = (2030 - self.ano)
        return f'Terá {idade_futura} anos em 2030'


name = input('Nome: ')
cidade_nascimento = input('Cidade natal: ')
ano_nascimento = int(input('Ano de nascimento: '))

pessoa1 = Pessoa(name,cidade_nascimento, ano_nascimento)
print(pessoa1.get_people())
print(pessoa1.set_people())