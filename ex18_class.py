# 18) Faça um programa que leia a nota de um aluno. Garanta que a nota seja um valor inteiro entre zero e 100. 
# Se o valor não estiver neste intervalo, informe que a nota é inválida. 
# Se a nota for maior que 60, informa que o aluno foi aprovado; caso contrário, informa que ele foi reprovado

'''class Aprovacao:
    def __init__(self, nota):
        self.nota = nota

    def confere_aprovacao(self):
        if self.nota <= 100 and self.nota >= 60:
            return f'Aprovado'
        elif self.nota <= 60 and self.nota >= 0:
            return f'Reprovado'
        else:
            return f'Nota inválida'
            '''

from class_18 import Aprovacao

nota = float(input('Digite sua nota: '))

aprovado = Aprovacao(nota)
aluno = aprovado.confere_aprovacao()
print(aluno)
