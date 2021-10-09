
class veiculo(object):
    def __init__(self, modelo, ano=2021, valor=0.00):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def get_modelo(self):
        return self.modelo
    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def get_ano(self):
        return  self.get_ano()
    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def get_valor(self):
        return self.valor
    def set_valor(self, novo_valor):
        if novo_valor > 0:
            self.valor = novo_valor
        else:
            print("ERRO! Valor incosistente, valor negativo.")

    def mostra_dados(self):
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"valor: {self.valor}")

    def retorna_dados(self):
        dados = f"{self.modelo}, {self.ano}, {self.valor}."
        return dados

    def aumento_valor(self,aumento_valor):
        self.valor += aumento_valor

    def compara_valor(self, outro_objeto):
        if self.valor > outro_objeto.valor:
            print("Carro masi caro: R$",self.valor)
            print("Carro mais barato R$",outro_objeto.valor)
        elif self.valor < outro_objeto.valor:
            print("Carro mais caro: R$", outro_objeto.valor)
            print("Carro mais barato: R$", self.valor)
        else:
            print("Tem o mesmo valor.")

















if __name__ == "__main__":
    carro1 = veiculo("HB", 2018, 50000.00)
    carro2 = veiculo("Corolla", 2019, 90000.00)
    print(carro1)
    print(carro2)
    retorno = carro1.get_modelo()
    print("modelo: ", retorno)
    print("modelo: ", carro2.get_modelo())
    carro1.set_modelo("HB20")
    print("Modelo: ", carro1.get_modelo())
    print("_"*30)
    carro1.mostra_dados()

    carro1.set_valor(52000.00)
    print("valor: ",carro1.get_valor())
    carro2.set_valor(-62000.00)
    print("valor: ",carro2.get_valor())
    print("_"*30)

    print(carro1.retorna_dados())

    carro3 = veiculo("TIGGO", 2020)
    print(carro3.retorna_dados())

    carro4 = veiculo("Pajeiro")
    print(carro4.retorna_dados())
