# 17) Desafio ex17.py:
# Dada uma equação de segundo grau, calcule suas raízes utilizando a fórmula de Bhaskara.
# (-b +- (√ (b²2 - 4ac)) / 2a

class Bhaskara():
    def __init__(self, valor_a, valor_b, valor_c):
        self.valor_a = valor_a
        self.valor_b = valor_b
        self.valor_c = valor_c

    def calcula_delta(self):
        delta = self.valor_b ** 2 - 4 * self.valor_a *self.valor_c
        return delta

    def calcula_primeira_raiz(self,delta):
        primeira_linha = (-self.valor_b + delta) 
        primeira_raiz = (primeira_linha / (2 * self.valor_a))
        return f'Primeira raiz: x1 = {primeira_raiz}'

    def calcula_segunda_raiz(self,delta):
        primeira_linha = (-self.valor_b - delta) 
        segunda_raiz = (primeira_linha / (2 * self.valor_a))
        return f'Segunda raiz: x2 = {segunda_raiz}'


print('Fórmula básica de uma equação de segundo grau: ax² + bx + c')
a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

formula = Bhaskara(a,b,c)
delta = formula.calcula_delta()
raiz1 = formula.calcula_primeira_raiz(formula.calcula_delta())
raiz2 = formula.calcula_segunda_raiz(formula.calcula_delta())

print(f'Equação de segundo grau: {a}x² + {b}x +{c}')
print(f'Delta: {delta}')
print(raiz1)
print(raiz2)