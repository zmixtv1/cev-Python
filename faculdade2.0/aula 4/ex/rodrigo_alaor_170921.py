
class som_grave (object):
    def __init__(self, modelo, potencia, tamanho, valor):
        self.modelo = modelo
        self.potencia = potencia
        self.tamanho = tamanho
        self.valor = valor



    def get_modelo(self):
        return self.modelo
    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def get_potencia(self):
        return self.potencia
    def set_potencia(self, nova_potencia):
        self.potencia = nova_potencia

    def get_tamanho(self):
        return self.tamanho
    def set_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho

    def get_valor(self):
        return self.valor
    def set_valor(self, novo_valor):
        self.modelo = novo_valor

    def mostra_dados(self):
        print(f"Modelo: {self.modelo}")
        print(f"potencia: {self.potencia} rms")
        print(f"tamanho: {self.tamanho}")
        print(f"valor: R$ {self.valor}")

    def retorna_dados(self):
        dados = f"{self.modelo}, {self.potencia} rms, {self.tamanho}, R$ {self.valor}."
        return dados





if __name__ == "__main__":
    grave1 = som_grave("Marauder", 5400, 12, 799.00)
    grave2 = som_grave("Zetta", 800, 12, 899.00)

    grave1.mostra_dados()
    grave2.mostra_dados()
    print("_"*30)
    print(grave1.retorna_dados())
    print(grave2.retorna_dados())
