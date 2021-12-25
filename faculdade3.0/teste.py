
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
    def set_qtd_portas(self,n_qtd):
        if n_qtd < 2 and n_qtd > 4:
            print("Quantidade de portas invalida.")
        else:
            self.qtd_portas = n_qtd

        return self.qtd_portas


    def calcula_ipva(self):
        ipva = self.preco * 0.03
        print(f"O valor do IPVA é {ipva}")

class onibus(veiculo):
    def __init__(self,placa, preco, capacidade):
        self.capacidade = capacidade
        super().__init__(placa,preco)

    def get_capacidade