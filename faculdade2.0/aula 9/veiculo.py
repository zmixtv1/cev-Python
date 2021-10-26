
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

    def atualiza_valor(self, vlr_aumento):
        if isinstance(vlr_aumento,(int,float)):
            if vlr_aumento > 0:
                self.valor += vlr_aumento
            else:
                print("Erro: valor Negativo.")
        else:
            print("Erro: Valor não é int nem float")

    def atualiza_valor_pct(self, pct):
        if pct > 0:
            self.valor = self.valor + self.valor * pct /100
        else:
            print("Erro: valor negativo")

    def situacao(self):
        if self.km == 0:
            print("Veiculo zero")
        elif self.km <= 20000:
            print("Veiculo seminovo")
        else:
            print("Veículo Usado.")
            


class carro(veiculo):
    def __init__(self,valor, modelo, km=1,qtd_portas=4):
        super().__init__(valor,modelo,km)
        self.qtd_portas = qtd_portas

    def get_qtd_portas(self):
        return self.qtd_portas


    def __str__(self):
        s = f"valor: {self.valor}, Modelo: {self.modelo}, KM: {self.km}, Qtd.portas: {self.qtd_portas}"
        return s

class moto(veiculo):
    def __init__(self, valor, modelo, km=1, cilindradas=2):
        super().__init__(valor, modelo, km)
        self.cilindradas = cilindradas

    def get_cilindradas(self):
        return self.cilindradas
    def set_silindradas(self,n_cilindrada):
        self.cilindradas = n_cilindrada

    def __str__(self):
        s = f"valor: {self.valor}, Modelo: {self.modelo}, KM: {self.km}, cilindradas: {self.cilindradas}"
        return s














if __name__ == "__main__":
    c1 = carro(990000, "Civic", 1000, 4)
    print(c1)
    print(f"Modelo: {c1.get_modelo()}")
    c2 = carro(100000, "corola", 0)
    print(c2)
    print(f"Modelo: {c2.get_modelo()}")
    c3 = carro(70000,"HB20")
    print(c3)
    print(f"Modelo: {c3.get_modelo()}")

    m1 = moto(30000, "BMW", 5000, 10)
    print(m1)
    m2 = moto(32000, "cbs", 12000, 400)
    print(m2)
    print(vars(c1))
    print(c1.__dict__)

    c1.atualiza_valor(250)
