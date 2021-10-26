
class veiculo(object):
    def __init__(self, valor, modelo,km=1):
        self.valor = valor
        self.modelo = modelo
        self.km = km

    def get_valor(self):
        return self.valor
    def set_valor(self,n_valor):
        self.valor = n_valor
        return self.valor
    def get_modelo(self):
        return self.modelo
    def get_km(self):
        return self.km


class carro(veiculo):
    def __init__(self,valor, modelo, km=1,qtd_portas=4):
        super().__init__(valor,modelo,km)
        self.qtd_portas = qtd_portas




if __name__ == "__main__":
     