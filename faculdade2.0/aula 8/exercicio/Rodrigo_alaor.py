
class jogo(object):
    def __init__(self, ano, criador, valor=2.00):
        self.ano = ano
        self.criador = criador
        self.valor = valor

    def get_ano(self):
        return self.ano

    def get_criador(self):
        return self.criador

    def get_valor(self):
        return self.valor

    def set_valor(self,n_valor):
        self.valor = n_valor
        return self.valor


class pc(jogo):
    def __init__(self, ano, criador, valor=2.00, tem_placa='Nao'):
        self.tem_placa = tem_placa.lower()
        super().__init__(ano, criador, valor)

    def pode_jogar(self):
        if self.tem_placa == "sim":
            print("Pode, roda Jogos")
        else:
            print("Não pode, não roda Jogos")

    def __str__(self):
        s = f"Ano: {self.ano}, Criador: {self.criador}, Valor: {self.valor}, Tem placa: {self.tem_placa}."
        return s


class console(jogo):
    def __init__(self, ano, criador, valor=2.00, qtd_controle=1):
        self.qtd_controle = qtd_controle
        super().__init__(ano, criador, valor)

    def get_qtd_controles(self):
        return self.qtd_controle
    def set_qtd_controles(self,n_qtd):
        self.qtd_controle = n_qtd
        return self.qtd_controle

    def players(self):
        if self.qtd_controle == 1:
            print("Pode jogar somente um player")
        elif self.qtd_controle == 2:
            print("Pode jogar somente dois players")
        elif self.qtd_controle == 3:
            print("Pode jogar somente três players")
        elif self.qtd_controle == 4:
            print("Pode jogar somente quatro players")
        else:
            print("Erro: O maximo de controles disponiveis são 4.")


    def __str__(self):
        s = f"Ano: {self.ano}, Criador: {self.criador}, Valor: {self.valor}, Quantidade de controles: {self.qtd_controle}."
        return s





if __name__ == '__main__':
    j1 = pc(2002,"Rodrigo", 250.00, "Sim")
    j2 = console(2005, "Lucas", 64.00, 3)

    print(j1.get_ano())
    print(j1.get_criador())
    print(j1.get_valor())
    j1.set_valor(300.00)

    print("_+"*30)

    print(j2.get_ano())
    print(j2.get_criador())
    print(j2.get_valor())
    j2.set_valor(150.00)

    print("_+" * 30)

    j1.pode_jogar()
    print(j1)

    print("_+" * 30)

    j2.get_qtd_controles()
    j2.set_qtd_controles(3)
    j2.players()
    print(j2)
