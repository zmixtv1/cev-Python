'''
class empregado(object):
    def __init__(self,nome, idade=18, salario=800):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_salario(self):
        return self.salario

    def set_nome(self,n_nome):
        self.nome = n_nome
        return n_nome

    def set_idade(self,n_idade):
        self.idade = n_idade
        return self.idade

    def set_salario(self,n_salario):
        if self.salario <= 1000:
            self.salario = n_salario
        elif self.salario >= 10000:
            self.salario += (n_salario/2)
        else:
            print(f"Salario não alterado")
        return self.salario

    def aumento_salarial(self,prct):
        self.salario += (self.salario * (prct/100))
        return f"Teve aumento de {prct}% valor atualizado = {self.salario}"

    def sala_anual(self):
        tot = self.salario * 12
        return f"total = {tot}"

    def decimo_terceiro(self):
        tot = self.salario * 11
        d3 = self.salario * 2
        tot += d3
        return f"O valor do decimo terceiro é de {d3}\nO valor anual com o decimo terceiro é de {tot}"



if __name__ == "__main__":

    objeto1 = empregado("Lucas")
    objeto2 = empregado("Rodrigo",19)
    objeto3 = empregado("Maria",salario=3000)

    print(objeto1.get_nome())
    print(objeto1.get_idade())
    print(objeto1.get_salario())

    print(objeto1.set_nome("Rodrigo"))
    print(objeto1.set_idade(20))
    print(objeto1.set_salario(5000))

    print(objeto1.aumento_salarial(10))
    print(objeto1.sala_anual())
    print(objeto1.decimo_terceiro())
'''


class pessoa(object):

    qtd = 0
    @classmethod
    def quantidade(cls):
        return f"Pessoas cadastrados: {cls.qtd}"

    def __init__(self,nome):
        self.nome = nome
        pessoa.qtd+=1

    def get_nome(self):
        return self.nome
    def set_nome(self,n_nome):
        self.nome = n_nome
        return self.nome


class professor(pessoa):
    def __init__(self,nome,qtd_turma):
        self.qtd_turma = qtd_turma
        super().__init__(nome)

    def set_qtd_turma(self,n_qtd):
        if self.qtd_turma <= 2:
            self.qtd_turma = n_qtd
            return f"turma adicionada"
        elif self.qtd_turma < 5:
            self.qtd_turma = n_qtd
            return f"Quantidade de turma adicionada"
        else:
            return f"Quantidade de turma lotada"

    def rendimentos(self):
        tot = (self.qtd_turma*800)
        return f"você tem {self.qtd_turma} turmas e vai receber R${tot}"


class funcionario(pessoa):
    def __init__(self,nome,salario:float=800):
        self.salario = salario
        super().__init__(nome)

    def set_salario(self,n_salario):
        if n_salario < self.salario:
            return f"Salario não alterado"
        elif self.salario == n_salario:
            return f"Salario igual, não alterado"
        else:
            self.salario = n_salario
            return f"Salario alterado para {self.salario}"

    def get_salario(self):
        return self.salario


if __name__ == "__main__":

    c1 = pessoa("Lucas")
    c2 = professor("Utabajara",3)
    c3 = funcionario("Pedro")

    print(c1.get_nome())     #get do nome
    print(c1.set_nome("Mateus"))    #set do nome

    print(c2.get_nome())    #get do nome
    print(c2.set_nome("Rodrigo"))   #set do nome
    print(c2.set_qtd_turma(7))  #set qunatidade de turma
    print(c2.rendimentos()) #rendimento baseado em qunatidade de turmas

    print(c3.get_nome())    #get do nome
    print(c3.set_nome("Mariana"))   #set do nome
    print(c3.get_salario()) #get salario
    print(c3.set_salario(2000)) #set salario

    print(c1.quantidade()) #pessoas cadastradas
