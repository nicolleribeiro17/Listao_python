# 17) Desafio ex17.py:
# Dada uma equação de segundo grau, calcule suas raízes utilizando a fórmula de Bhaskara.
# (-b +- (√ (b²2 - 4ac)) / 2a

def raizes(a,b,c):
  delta = b**2 - 4*a*c
  #primeira raiz
  x1 = (-b + delta) / 2*a
  #segunda raiz 
  x2 = (-b - delta) / 2*a

  print('\nValor da primeira raiz x1: {0}'.format(x1))
  print('Valor da segunda raiz x2: {0}'.format(x2))


print('Fórmula básica de uma equação de segundo grau: ax² + bx + c\n')
a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

print(f'Equação de segundo grau: {a}x² + {b}x +{c}')

raizes(a,b,c)