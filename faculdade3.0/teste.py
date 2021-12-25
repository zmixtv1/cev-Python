
class veiculo(object):

    def __init__(self,placa, preco):
        self.placa = placa
        self.preco = preco

    def get_placa(self):
        return self.placa
    def set_placa(self,n_placa):
        self.placa = n_placa

    def get_preco(self):
        return self.preco
    def set_preco(self, n_preco):
        self.preco = n_preco

class carro(veiculo):
    def __init__(self, placa, preco, qtd_portas):
        self.qtd_portas = qtd_portas
        super().__init__(placa,preco)

    