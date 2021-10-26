"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

Monitoria (plantão de dúvidas): https://monitoriaceub.github.io/Monitoria/index.html

- Com base nos conceitos de POO, vamos trabalhar com duas classes (entidades).
implemente a entidade funcionario com estas características cpf, nome e salario.
E a entidade gerente com estas características cpf, nome, salario, senha e
quantidade de funcionários que ele gerencia. Implemente estes itens.

...
15-h1- Conceito de herança: eliminar código repetido e herdar atributos e métodos
16- A subclasse Gerente herda da superclasse Funcionario
17- Altere o construtor da subclasse Gerente.
18- Rode a função main com as alterações realizadas.
"""
class Funcionario(object):                          # Superclasse ou classe pai
    def __init__(self, cpf, nome, salario=0.0):     # Construtor
        self.cpf = cpf
        self.nome = nome                            # Atributos de instância
        self.salario = salario
    def get_cpf(self):
        return self.cpf
    def get_nome(self):                             # Consulta
        return self.nome
    def set_nome(self, novo_nome):                  # Altera na memória
        self.nome = novo_nome
    def get_salario(self):
        return self.salario
    def __str__(self):                              # Método mágico ou método dunder
        # s = 'Nome: ' + self.nome+ ',  CPF: ' + self.cpf+ ', salário: ' + str(self.salario)
        # s = "Nome: {}, CPF: {}, salario: {:.2f}" .format(self.nome, self.cpf, self.salario)
        s = f"Nome: {self.nome}, CPF: {self.cpf}, salario: {self.salario:.2f}"  # f-string
        return s                                    # As linhas acima são equivalentes
# A sublcasse Gerente (filha) herda da superclasse Funcionario (pai)
class Gerente(Funcionario):                         # class NomeSubclasse(NomeSuperclasse):
    def __init__(self, cpf, nome, salario, senha, qtd_gerencia=0):
        # self.cpf = cpf                            # Elimina atributos repetidos
        # self.nome = nome
        # self.salario = salario
        super().__init__(cpf, nome, salario)              # Chama o construtor da superclasse
        # Funcionario.__init__(self, cpf, nome, salario)  # Chama o construtor da superclasse
        self.senha = senha
        self.qtd_gerencia = qtd_gerencia
    # def get_cpf(self):                            # Elimina métodos repetidos
    #     return self.cpf
    # def get_nome(self):
    #     return self.nome
    # def set_nome(self, novo_nome):
    #     self.nome = novo_nome
    # def get_salario(self):
    #     return self.salario
    def get_qtd_gerencia(self):
        return self.qtd_gerencia
    def autentica(self):                            # Solução 1
        senha = input("Senha: ")
        if self.senha == senha:
            print("Acesso permitido.")
            return True
        else:
            print("Acesso negado.")
            return False
    # def autentica(self):                          # Solução 2
    #     senha = input("Insira a senha: ")
    #     while senha != self.senha:
    #         print("\033[31mAcesso negado!\033[m")
    #         senha = input("Insira a senha: ")
    #     else:
    #         print("\033[32mAcesso permitido!\033[m")
    #         return True

if __name__ == '__main__':
    f1 = Funcionario('123', 'Paulo', 1000.0)        # Cria o objeto f1, chama o construtor
    print(f1)                                       # print(f1.__str__())   # Teste
    # <__main__.Funcionario object at 0x00000159D5FFB2C8>
    print(f'Nome: {f1.get_nome()}')
    print(f'CPF: {f1.get_cpf()}')
    print('Salário:', f1.get_salario())
    r = f1
    print(r)                                        # print(r.__str__())
    print(f1)                                       # print(f1.__str__())
    g1 = Gerente('234', 'Paula', 3000.0, 's1', 5)   # g1 é um objeto da classe Gerente
    print(g1)                                       # print(g1.__str__())   # Teste
    print(f'g1 - CPF: {g1.get_cpf()}')
    print('g1 - Nome:', g1.get_nome())
    print(g1.__str__())                             # print(g1), conseguiu usando o __str__?
    r = g1.autentica()                              # O método retorna True ou False
    if r:                                           # if r == True:
        pass
    print(r)                                        # Linhas equivalentes
    print(g1.autentica())
    # r = f1.autentica()                            # Erro, Funcionario não tem método autentica
    # AttributeError: 'Funcionario' object has no attribute 'autentica'
    g2 = Gerente('34', 'Paulo', 5000.0, 'g2', 3)
    print(g2.__str__())                             # print(g2), conseguiu usando o __str__?
    print('g2 - Nome:', g2.get_cpf())
    print('g2 - Nome:', g2.get_nome())
