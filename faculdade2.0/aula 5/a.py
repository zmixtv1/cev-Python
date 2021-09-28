"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

Monitoria (plantão de dúvidas): https://monitoriaceub.github.io/Monitoria/index.html

- Com base nos conceitos de POO, implemente a entidade pessoa com estas características:
nome, peso, altura e data de nascimento. Resolva os itens:

1- Crie a classe Pessoa
2- Crie o método construtor: ele recebe quatro parâmetros que serão armazenados nos atributos.
   No construtor, crie os três atributos da classe (nome, peso, altura e data de nascimento)
3- No método main, crie o objeto pessoa1 e passe os argumentos.
4- Mostre o objeto criado, o objeto pessoa1, teste (rode) a classe
5- Crie os métodos get (consultar) e set (alterar) para os atributos nome e dta_nascimento.
6- No main, teste os métodos gets dos atributos da classe Pessoa (consulte e mostre)
   Mostre o atributo nome, altere o nome do objeto pessoa1 e mostre o atributo dta_nascimento
7- Use o método set para alterar o valor do atributo dta_nascimento para 2005-12-13. Teste
8- Crie o método IMC (Índice de Massa Corporal), ele recebe o objeto, calcula e retorna o valor
   do imc. O IMC é calculado dividindo o peso (em kg) pela altura ao quadrado (em metros).
9- No programa (main), crie o objeto pessoa2 e passe os argumentos
10- Teste o item anterior, ou seja, mostre o valor dos atributos do objeto pessoa2
11- Altere o construtor para ele instanciar um objeto sem a dta_nascimento,
    valor default 2000-01-21. Ele recebe somente o nome, o peso e a altura. Teste
12- Crei o método set_nome com crítica, evitar dados inconsistentes. Teste
13- Sobrescreva o método especial __str__ . Ele recebe o objeto e retorna os dados de uma
     pessoa (nome, peso e data de nascimento). Teste.
14- Crie o método calcula_idade, ele recebe o objeto e retorna a idade da pessoa. Teste abaixo:
    No final do main, altere a data da pessoa1 para: (2000, 11, 13). Qual a idade da pessoa1?
15- Crie o método mais_velho, ele compara a dta_nascimento de duas pessoas quaisquer e
    mostra a dta_nascimento do mais velho ou a mensagem "As datas são iguais.". Teste.

"""

import datetime
class Pessoa(object):  # Nome de classe começa com letra maiúscula. E as outras letras minúsculas.
    # def __init__(self, nome, peso, altura, dta_nascimento):   # Método construtor
    def __init__(self, nome, peso, altura, dta_nascimento=datetime.date(2000, 1, 21)):  # default
        self.nome = nome                                        # Atributos
        self.peso = peso
        self.altura = altura
        self.dta_nascimento = dta_nascimento
    def get_nome(self):                                         # Métodos gets e sets
        return self.nome
    # def set_nome(self, novo_nome):                              # Sem crítica
    #     self.nome = novo_nome
    def set_nome(self, p_nome):                                 # Com crítica, solução 1
        # if type(p_nome) == str:                                 # Duas linhas equivalentes
        if isinstance(p_nome, str):
            self.nome = p_nome
        else:
            print('Erro: nome deve ser string.')
    # def set_nome(self, novo_nome):                              # Com crítica, solução 2
    #     if isinstance(novo_nome, str):
    #         if len(novo_nome) >= 3:                   # RN: nome precisa ter pelo menos 3 letras
    #             self.nome = novo_nome
    #         else:
    #             print('ERRO: Nome inválido')
    #     else:
    #         print('ERRO: Tipo inválido')
    def get_dta_nascimento(self):                               # Consultar
        return self.dta_nascimento
    def set_dta_nascimento(self, nova_data):                    # Alterar
        self.dta_nascimento = nova_data
    def imc(self):                                              # Método funcional
        # vl_imc = self.peso / self.altura ** 2                 # 1
        # vl_imc = self.peso / pow(self.altura, 2)              # 2
        vl_imc = self.peso / (self.altura * self.altura)        # 3 (Parênteses obrigatórios)
        return vl_imc
        # return self.peso / (self.altura * self.altura)        # 4 (Parênteses obrigatórios)
    def __str__(self):                            # Sobrescrevendo o método especial __str__
        # s = self.get_nome() + ' ' + str(self.peso) + ', ' + str(self.get_dta_nascimento())
        # s = "{} {}, {}" .format(self.nome, self.peso, self.dta_nascimento)  # .format
        # s = f"{self.get_nome()}, {self.peso} {self.get_dta_nascimento()}"   # Usa métodos gets
        s = f"{self.nome}, {self.peso}, {self.dta_nascimento}"                # f-string
        return s
        # return f"Nome: {self.nome}, Peso: {self.peso}, Nascimento: {self.dta_nascimento}"
    def calcula_idade(self):                                # Método funcional
        hoje = datetime.date.today()                        # Data completa de hoje (ano, mes, dia)
        idade = hoje.year - self.dta_nascimento.year        # year pega o ano de uma data
        # return idade                                        # Solução incompleta
        # Dica: Teste os meses da data de hoje e da data de nascimento.
        if hoje.month < self.dta_nascimento.month:          # month pega o mês de uma data
            idade -= 1
        # Dica: Se os meses forem iguais, precisa testar os dias também.
        elif hoje.month == self.dta_nascimento.month and hoje.day < self.dta_nascimento.day:
            idade -= 1
        return idade
    # pessoa1.mais_velho(pessoa2)                             # Chamada do método no main
    def mais_velho(self, obj):                 # Solução 1, usando o atributo self.dta_nascimento
        if self.dta_nascimento < obj.dta_nascimento:
            print("dta_nascimento mais velho: ", self.dta_nascimento)
            print("dta_nascimento mais novo: ", obj.dta_nascimento)
        elif obj.dta_nascimento < self.dta_nascimento:
            print("dta_nascimento mais velho: ", obj.dta_nascimento)
            print("dta_nascimento mais novo: ", self.dta_nascimento)
        else:
            print("As datas sao iguais.")
    # def mais_velho(self, obj):               # Solução 2, usando o método calcula_idade()
    #     if self.calcula_idade() < obj.calcula_idade():
    #         print("dta_nascimento mais velho: ", obj.dta_nascimento)
    #         print("dta_nascimento mais novo: ", self.dta_nascimento)
    #     elif obj.calcula_idade() < self.calcula_idade():
    #         print("dta_nascimento mais velho: ", self.dta_nascimento)
    #         print("dta_nascimento mais novo: ", obj.dta_nascimento)
    #     else:
    #         print("As datas sao iguais.....")


if __name__ == '__main__':                                      # Atalho: mai <tab>
    dta_nascimento_1 = datetime.date(1993, 12, 13)              # datetime.date(ano, mes, dia)
    pessoa1 = Pessoa("Carlos", 71, 1.80, dta_nascimento_1)      # Chama construtor (__init__)
    # pessoa1 = Pessoa("Carlos", 71, 1.80, datetime.date(1993, 12, 13))  # Equivalente as 2 linhas
    print(pessoa1)  # print(pessoa1.__str__())                  # Chama o método __str__
    '''   <__main__.Pessoa object at 0x0000014E7C0F9FD0>   '''
    nome = pessoa1.get_nome()                                   # Usando variável
    print("- Pessoa 1:\nNome:", nome)
    # print("- Pessoa 1:\nNome:", pessoa1.get_nome())             # Equivalente as duas anteriores
    print("dta_nascimento:", pessoa1.get_dta_nascimento())      # Direto no print
    pessoa1.set_nome("Ailton")                                  # Pode usar um input
    print('Nome:', pessoa1.get_nome())                          # Teste
    dta_nascimento_2 = datetime.date(2005, 12, 23)              # Solução 1
    pessoa1.set_dta_nascimento(dta_nascimento_2)
    # ano = int(input('Ano: '))                                 # Solução 2
    # mes = int(input('Mês: '))
    # dia = int(input('Dia: '))
    # dta_nascimento_2 = datetime.date(ano, mes, dia)
    # pessoa1.set_dta_nascimento(dta_nascimento_2)
    pessoa1.set_dta_nascimento(datetime.date(2005, 12, 23))     # Solução 3
    print("dta_nascimento:", pessoa1.get_dta_nascimento())      # Teste
    print('IMC:', pessoa1.imc())                                # IMC: 21.91358024691358
    print(f'IMC: {pessoa1.imc()}')                              # IMC: 21.91358024691358
    print(f'IMC: {pessoa1.imc():.2f}')                          # IMC: 21.91, f-string
    dta_nascimento_3 = datetime.date(2010, 11, 23)
    pessoa2 = Pessoa("Maria", 63, 1.65, dta_nascimento_3)      # chama método __init__ (construtor)
    print("- Pessoa 2:\nNome: ", pessoa2.get_nome())            # Teste
    print("dta_nascimento: ", pessoa2.get_dta_nascimento())
    pessoa3 = Pessoa("Ana", 61, 1.69)                           # Passando só três argumentos
    print('- Pessoa 3:\nData Nascimento:', pessoa3.get_dta_nascimento())
    pessoa1.set_nome(2.3)                                       # Tipo do argumento errado
    print('Nome:', pessoa1.get_nome())                          # Teste
    pessoa1.set_nome("Rogério")                                 # Tipo do argumento correto
    print('Nome:', pessoa1.get_nome())                          # Teste
    print(pessoa3.__str__())                        # Linhas equivalentes, __str__() é opcional
    print(pessoa3)
    print(pessoa1)
    pessoa1.set_dta_nascimento(datetime.date(2000, 11, 13))
    # pessoa1.set_dta_nascimento(datetime.date(2000, 9, 24))
    print("Idade 1:", pessoa1.calcula_idade())
    print("Idade 2:", pessoa2.calcula_idade())
    print("Idade 3:", pessoa3.calcula_idade())
    pessoa1.mais_velho(pessoa2)                                 # objeto1.nome_metodo(objeto2)
    pessoa1.mais_velho(pessoa3)
    pessoa2.mais_velho(pessoa3)
