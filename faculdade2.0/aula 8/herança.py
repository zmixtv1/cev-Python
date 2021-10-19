

class funcionario(self):
    def __init__(self, cpf, nome ,salario=0.0):
        self.cpf = cpf
        self.nome = nome
        self.salario = salario

    def get_cpf(self):
        return self.cpf

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_salario(self):
        return self.salario





class gerente(object):
    def __init__(self,cpf, nome, salario, senha, qtd_gerencia=0):
        self.cpf = cpf
        self.nome = nome
        self.salario = salario
        self.senha= senha
        self.qtd_gerencia = qtd_gerencia

    def get_cpf(self):
        return self.cpf
    def get_nome(self):
        return self.nome
    def set_nome(self,novo_nome):
        self.nome = novo_nome
    def get_salario(self):
        return self.salario
    def get_qtd_gerencia(self):
        return self.qtd_gerencia

    def autentica(self):
        senha = input("Senha: ")








if __name__ == '__main__':
    f1 = funcionario("123", "Paulo", 1000.0)
    print(f1)
    print(f"nome: {f1.get_nome()}")
    print(f"CPF: {f1.get_cpf()}")
    print(f"Salario:", f1.get_salario())
    r = f1
    print(r)
    print(f1)
    g1 = gerente("234", "Paula", 3000.0, "s1",5)
    print(g1)
