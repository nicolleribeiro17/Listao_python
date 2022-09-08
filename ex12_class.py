#12) Programa Python no arquivo ex12.py: Este programa irá calcular a área de um triângulo. Peça para a pessoa informar a medida 
# numérica da base do triângulo, depois colete o valor da altura. Apresente o valor da área do triângulo.

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcula_area(self):
        area = ((self.base * self.altura) / 2)
        return f'Área do triângulo: {area}'

base1 = int(input("Digite um valor para a base: "))
altura1 = int(input("Digite um valor para a altura: "))

area1 = Triangulo(base1, altura1)
print(area1.calcula_area())

