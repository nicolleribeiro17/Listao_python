class Aprovacao:
    def __init__(self, nota):
        self.nota = nota

    def confere_aprovacao(self):
        if self.nota <= 100 and self.nota >= 60:
            return f'Aprovado'
        elif self.nota <= 60 and self.nota >= 0:
            return f'Reprovado'
        else:
            return f'Nota inválida'