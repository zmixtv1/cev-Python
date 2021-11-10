class Veiculo:
    quantidade = 0

    @classmethod
    def contador(cls):
        return (f'Veiculos cadastrados: {cls.quantidade}')

    def __init__(self, placa, preco):
        self.placa = placa
        self.preco = preco
        Veiculo.quantidade += 1

    def get_placa(self):
        return self.placa

    def set_placa(self, nova_placa):
        self.placa = nova_placa

    def get_preco(self):
        return self.preco

    def set_preco(self, novo_preco):
        self.preco = novo_preco


class carro(Veiculo):
    def __init__(self, placa, preco, quantidade_portas):
        super().__init__(placa, preco)
        self.placa = placa
        self.preco = preco
        self.quantidade_portas = quantidade_portas

    def get_quantidade_portas(self):
        return self.quantidade_portas

    def set_quantidade_portas(self, nova_quantidade_portas):
        self.quantidade_portas = nova_quantidade_portas
        if self.quantidade_portas < 2:
            print(f'Carro deve ter no minimo 2 portas')
        else:
            print(self.quantidade_portas)

    def calcula_ipva(self):
        ipva = self.preco * 1.03
        return ipva


class onibus(Veiculo):
    def __init__(self, placa, preco, capacidade):
        super().__init__(placa, preco)
        self.capacidade = capacidade

    def get_capacidade(self):
        return self.capacidade

    def set_capacidade(self, nova_capacidade):
        self.capacidade = nova_capacidade
        if self.capacidade > 40:
            print(f'Onibus superlotado!')
        return self.capacidade

    def __str__(self):
        return f'placa: {self.placa}, {self.preco}, {self.capacidade}'


if __name__ == '__main__':
    carro1 = carro("PAN8392", 70000, 2)
    onibus1 = onibus("RIO4B96", 130000, 50)

    print(f'IPVA do Carro 1: {carro1.calcula_ipva()}')
    print(f'Situação do onibus: {onibus1.set_capacidade(15)}')