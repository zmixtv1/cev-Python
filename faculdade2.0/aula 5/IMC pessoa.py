import datetime

class pessoa(object):
    def __init__(self, nome, peso, altura, data_de_nascimento):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.data_de_nascimento = data_de_nascimento


    def get_nome(self):
        return self.nome
    def set_nome(self,novo_nome):
        self.nome = novo_nome
    def get_data_de_nascimento(self):
        return self.data_de_nascimento
    def set_data_de_nascimeto(self,nova_data):
        self.data_de_nascimento = nova_data
    def imc(self):
        vl_imc = self.peso/(self.altura ** 2)
        return vl_imc



if __name__ == "__main__":
    data_de_nascimento = datetime.date(1993,12,13)
    pessoa1 = pessoa("Rodrigo", 50, 1.83, data_de_nascimento)
    print(pessoa1)

    nome = pessoa1.get_nome()
    print(f"Pessoa 1 = {nome}")
    pessoa1.set_nome("Jorge")

    