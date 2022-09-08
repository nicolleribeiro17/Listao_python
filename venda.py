class Venda:
    def __init__(self, valor, vendedor):
        self.valor = valor
        self.vendedor = vendedor
    
    def calcula_comissao(self):
        if self.valor >= 50000:
            comissao = (self.valor + ( self.valor * 0.3))
            return f'Para a venda concluida pelo vendedor(a) {self.vendedor} a comissão é de: R${comissao}.'
        elif self.valor >= 10000 and self.valor <= 50000:
            comissao = (self.valor + (self.valor * 0.25))
            return f'Para a venda concluida pelo vendedor(a) {self.vendedor} a comissão é de: R${comissao}.'
        elif self.valor >= 5000 and self.valor <= 10000:
            comissao = (self.valor + (self.valor * 0.20))
            return f'Para a venda concluida pelo vendedor(a) {self.vendedor} a comissão é de: R${comissao}.'
        elif self.valor >= 1000 and self.valor <= 5000:
            comissao = (self.valor + (self.valor * 0.20))
            return f'Para a venda concluida pelo vendedor(a) {self.vendedor} a comissão é de: R${comissao}.'
        else:
            return f'Venda realizada pelo(a) {self.vendedor} não é passivel de comissão.'


        
