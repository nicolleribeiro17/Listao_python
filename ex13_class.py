# 13). Crie o seguinte programa Python no arquivo ex13.py: Colete a idade de 3 pessoas e mostre a média de suas idades.

class Media:
    def __init__(self, pessoa1, pessoa2, pessoa3):
        self.pessoa1 = pessoa1
        self.pessoa2 = pessoa2
        self.pessoa3 = pessoa3
    
    def mean(self):
        media = ((self.pessoa1 + self.pessoa2 + self.pessoa3) / 3)
        return f'Média das idades: {media}'

idade1 = int(input('Digite a primeira idade: '))
idade2 = int(input('Digite a segunda idade: '))
idade3 = int(input('Digite a terceira idade: '))

media_idades = Media(idade1, idade2, idade3)
print(media_idades.mean())