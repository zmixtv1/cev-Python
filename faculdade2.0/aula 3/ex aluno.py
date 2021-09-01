


class aluno(object):
    def __init__(self, nome="undefined", mensalidade=1000.0, idade=18):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade

    def get_nome(self):
        return self.nome
    def set_nome(self,novo_nome):
        self.nome = novo_nome
    def get_mensalidade(self):
        return self.mensalidade
    def ser_mensalidade(self, valor):
        self .mensalidade = valor
    def get_idade(self):
        return  self.idade
    def set_idade(self, nova_idade):
        self.idade = nova_idade
    def mostra_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Mensalidade: {self.mensalidade}")
        print(f"Idade: {self.idade}")
    def mostra_dados2(self):
        print(f"Nome: {self.get_nome()}")
        print(f"Mensalidade: {self.get_mensalidade()}")
        print(f"Idade: {self.get_idade()}")
    def retorna_dados(self):
        dados = f"{self.nome}, {self.mensalidade}, {self.idade}."
        return dados
    def aumento_mensalidade_valor(self,valor):
       self.mensalidade += valor
    def aumento_mensalidade_porcet(self,porc):
        self.mensalidade += self.mensalidade * porc / 100
    def pode_cnh(self):
        if self.idade >= 18:
            print("Pode!")
        else:
            print("Não Pode!")













if __name__ == "__main__":
    aluno1 = aluno("Paulo", 1000.0, 21)
    aluno2 = aluno("Rodrigo", 900.0, 19)
    aluno3 = aluno("Alaor")
    aluno4 = aluno("Ana",idade=10)
    aluno5 = aluno("Lopes",idade=21)

    '''print("aluno 1:")
    print("Nome:", aluno1.get_nome())
    print(f"idade: {aluno1.get_idade()}")
    print(f"Nome: {aluno2.get_nome()} \nIdade: {aluno2.get_idade()} \nMensalidade: {aluno2.get_mensalidade()}")

    nome = input("Novo Nome: ")
    aluno1.set_nome(nome)
    print(f"Nome: {aluno1.get_nome()}\n")
    aluno2.set_nome("Alice") 

    aluno2.mostra_dados()'''

    print(f"Dados: {aluno1.retorna_dados()}")
    print(aluno2.retorna_dados())
    aluno2.aumento_mensalidade_valor(110)
    print(aluno2.retorna_dados())
    aluno2.aumento_mensalidade_porcet(15)
    print(aluno2.retorna_dados())
    print(aluno3.retorna_dados())
    print(aluno5.retorna_dados())
    aluno2.pode_cnh()
    aluno4.pode_cnh()