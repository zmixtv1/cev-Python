
class veiculo(object):

    qtd = 0

    @classmethod
    def quantidade(cls):
        return f"Veiculos cadastrados: {cls.qtd}"

    def __init__(self,placa,ano=2005,preco=5000):
        self.placa = placa
        self.ano = ano
        self.preco = preco
        veiculo.qtd += 1

    def get_placa(self):
        return self.placa
    def set_placa(self,n_placa):
        if n_placa == self.placa:
            print("Placa identica ou já alterada")
        else:
            self.placa = n_placa
        return self.placa

    def atualiza_valor(self, vlr_aumento):
        if vlr_aumento < 0:
            print("valor invalido!")
        elif vlr_aumento > self.preco:
            resp = input(str("valor Muito alto\nDeseja realmente realizar esta operação: ")).upper()[0]
            if resp == "S":
                self.preco += vlr_aumento
                print("Valor atualizado")
            else:
                print("Operação cancelada")
        else:
            self.preco += vlr_aumento
            print("Valor Atualizado!")
        return self.preco

    "Desenvolva o método funcional promoção que recebe a porcentagem do desconto e atualiza o valor do veiculo, faça crítica."
    def promocao(self,pct_desconto):
        if pct_desconto < 0 or pct_desconto > 50:
            print("Desconto invalido.")
        else:
            self.preco = self.preco - (self.preco*(pct_desconto/100))
            print("Desconto feito.")

        return self.preco



if __name__ == "__main__":

    c1 = veiculo("axy1524")
    c2 = veiculo("jhv3246", preco=10000)

    print(c1.get_placa())

    print(c1.set_placa("abc1234"))

    print(c1. atualiza_valor(10000))

    print(c1.promocao(30))

    print(veiculo.quantidade())


'''
class herança(object):
    def __init__(self,nome,saldo):
        self.nome = nome
        self.saldo = saldo

    def get_nome(self):
        return self.nome
    def get_saldo(self):
        return self.saldo

    def set_nome(self,n_nome):
        self.nome = n_nome
        return self.nome
    def set_saldo(self,n_saldo):
        self.saldo = n_saldo
        return self.saldo

    def __str__(self):
        return f"Nome = {self.nome}\nSaldo: {self.saldo}"


class contacorrente(herança):
    def __init__(self,nome,saldo,cheque_especial):
        self.cheque_especial = cheque_especial
        super().__init__(nome,saldo)

    def get_cheque_especial(self):
        return self.cheque_especial
    def set_cheque_especial(self,n_cheque):
        if n_cheque < self.cheque_especial:
            print("valor é menor que o atual, operação cancelada.")
        else:
            self.cheque_especial = n_cheque
        return self.cheque_especial

    def saldo_total(self):
        tot = self.saldo + self.cheque_especial

        return f"O Total é {tot}"


    "faça um metodo investimento que tire o dinheiro da Conta Corrente e mostre o valor disponivel para resgate."
    def investimento(self,a1):
        if a1 > self.saldo:
            print(f"você não possui dinheiro suficiente")
        elif a1 < 0:
            print(f"valor invalido, tente novamente")
        else:
            print(f"você investiu em CDB 180 dias.")
            self.saldo -= a1
            a1 = a1*(102/100)
            print(f"O valor disponivel para resgate em 180 dias é R${a1}")


class poupanca(herança):
    def __init__(self,nome,saldo,prct_rendimento):
        self.prct_rendimento = prct_rendimento
        super().__init__(nome,saldo)

    def get_prct_rendimento(self):
        return self.prct_rendimento
    def set_prct_rendimento(self,n_prct):
        if n_prct < self.prct_rendimento:
            print("valor menor que o atual\nOperação cancelada")
        else:
            self.prct_rendimento = n_prct
        return self.prct_rendimento


    def saldo_atualizado(self):
        tot = self.saldo + (self.saldo*(self.prct_rendimento/100))
        return tot



if __name__ == "__main__":

    c1 = contacorrente("Lucas",5000,5000)
    c2 = poupanca("Rodrigo",3000,1.2)

    print(c1.get_nome())
    print(c1.set_nome("Carlos"))
    print(c1.get_saldo())
    print(c1.set_saldo(10000))
    print(c1.get_cheque_especial())
    print(c1.set_cheque_especial(6000))
    print(c1.saldo_total())
    c1.investimento(5000)

    print(c2.get_nome())
    print(c2.set_nome("Alaor"))
    print(c2.get_saldo())
    print(c2.set_saldo(50000))
    print(c2.get_prct_rendimento())
    print(c2.set_prct_rendimento(2))
    print(c2.saldo_atualizado())
'''
