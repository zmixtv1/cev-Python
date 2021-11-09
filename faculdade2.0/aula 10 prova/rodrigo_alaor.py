
'''
class conta_corrente(object):
    def __init__(self,nome_titular,n_conta,saldo=0.00):
        self.nome_titular = nome_titular
        self.n_conta = n_conta
        self.saldo = saldo


    def get_nome_titular(self):
        return self.nome_titular
    def get_n_conta(self):
        return self.n_conta
    def get_saldo(self):
        return self.saldo

    def set_nome_titular(self,novo_nome):
        self.nome_titular = novo_nome
        return self.nome_titular
    def set_n_conta(self,nova_conta):
        self.n_conta = nova_conta
        return self.n_conta

    def deposito(self,valor_deposito):
        self.saldo += valor_deposito


    def transferencia(self,outra_conta,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            outra_conta.deposito(valor)
            print(f"Foi transferido o valor de R${valor} na conta de {outra_conta.get_nome_titular()}")
        else:
            print("Saldo Insuficiente.")


if __name__ == "__main__":
    conta1 = conta_corrente("Rodrigo", 8321, 10000)
    conta2 = conta_corrente("Tepe", 7777)

    print("+_+"*30)

    print(conta1.get_nome_titular())
    print(conta1.get_n_conta())
    print(conta1.get_saldo())
    conta1.set_nome_titular("Kathleen")
    conta1.set_n_conta(3214)

    print("+_+" * 30)

    print(conta2.get_nome_titular())
    print(conta2.get_n_conta())
    print(conta2.get_saldo())
    conta2.set_nome_titular("Léo")
    conta2.set_n_conta(8923)

    print("+_+" * 30)

    conta1.deposito(240)
    conta2.deposito(240)

    conta1.transferencia(conta2,3000)
'''


class veiculo(object):

    qtd = 0

    @classmethod
    def quantidade(cls):
        return f"Veiculos cadastrados: {cls.qtd}"

    def __init__(self,placa,preco):
        self.placa = placa
        self.preco = preco
        veiculo.qtd += 1

    def get_placa(self):
        return self.placa

    def get_preco(self):
        return self.preco

    def set_placa(self,n_placa):
        self.placa = n_placa

    def set_preco(self,n_preco):
        self.preco = n_preco


class carro(veiculo):
    def __init__(self,placa, preco, qtd_portas):
        self.qtd_portas = qtd_portas
        super().__init__(placa,preco)

    def set_qtd_portas(self,n_qtd):
        if n_qtd < 2 and n_qtd > 4:
            print("Quantidade de portas invalidada")
        else:
            self.qtd_portas = n_qtd

        return self.qtd_portas

    def calcula_ipva(self):
        ipva = self.preco * 0.03
        print(f"o valor do ipva é {ipva}")


class onibus(veiculo):
    def __init__(self,placa, preco, capacidade):
        self.capacidade = capacidade
        super().__init__(placa, preco)

    def get_capacidade(self):
        return self.capacidade

    def set_capacidade(self,n_capaciade):
        self.capacidade = n_capaciade

    def __str__(self):
        p = f"Placa = {self.placa}, Preço = {self.capacidade}"
        return p


if __name__ == "__main__":

    c1 = carro("ab123",15000,4)
    c2 = onibus("cd456", 250000, 30)

    print("_+"*30)

    print(c1.get_placa())
    print(c1.get_preco())
    print(c1.set_qtd_portas(2))

    print("_+" * 30)

    print(c2.get_placa())
    print(c2.get_preco())

    print("_+" * 30)

    c1.calcula_ipva()

    print("_+" * 30)

    print(c2)

    c2.get_capacidade()
    c2.set_capacidade(15)

    print(c2)

