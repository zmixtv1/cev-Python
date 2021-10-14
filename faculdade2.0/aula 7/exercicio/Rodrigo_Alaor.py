

class serie(object):
    def __init__(self,nome,valor,ano=2020,temporada=1,duracao=40):
        self.nome = nome
        self.valor = valor
        self.ano = ano
        self.temporada = temporada
        self.duracao = duracao

    def get_nome(self):
        return self.nome
    def get_valor(self):
        return self.valor
    def get_ano(self):
        return self.ano
    def get_temporada(self):
        return self.temporada
    def get_duracao(self):
        return self.duracao

    def set_nome(self,n_nome):
        self.nome = n_nome
        return self.nome
    def set_ano(self,n_ano):
        self.ano = n_ano
        return self.ano
    def set_temporada(self,n_temporada):
        self.temporada = n_temporada
        return self.temporada
    def set_duracao(self,n_duracao):
        self.duracao = n_duracao
        return self.duracao
    def set_valor(self,n_valor):
        self.valor = n_valor
        return self.valor

    def retorna_dados(self):
        if self.valor < 80:
            dados = f"Nome: {self.nome}, Valor mensal: R${self.valor}, Anor: {self.ano}, Temporada: {self.temporada}, Duração: {self.duracao}min."
        else:
            dados = f"Nome: {self.nome}, Valor Anual: R${self.valor}, Anor: {self.ano}, Temporada: {self.temporada}, Duração: {self.duracao}min."
        return dados


    def compara_valor(self, outro_objeto):
        if self.valor > outro_objeto.valor:
            print("plataforma maus cara: R$", self.valor)
            print("plataforma mais barata: R$", outro_objeto.valor)
        elif self.valor < outro_objeto.valor:
            print("Plataforma mais cara: R$", outro_objeto.valor)
            print("plataforma mais barata: R$", self.valor)
        else:
            print("Tem o mesmo valor.")


    def get_opniao(self):

        if self.nome == "Round 6":
            print(f"{serie1.nome}: Não assisti a serie")
        elif self.nome == "Grey's Anatomy":
            print(f"{serie1.nome}: Se você gosta de series sobre hospitais, você vai amar esta série")

        elif self.nome == "Supernatural":
            print(f"{serie2.nome}:Super recomendo se você gosta de ação com aventura, a historia conta "
                  f"sobre dois irmão caçadores e sua jornada por salvar a terra dos monstros")
        elif self.nome == "The Boys":
            print(
                f"{serie2.nome}: Esta serie mostra o lado inverso dos super-heróis, os heróis que tambem fazem cagadas")

        elif self.nome == "Os Simpsons":
            print(f"{serie3.nome}:Otima serie para assistir com a família")

        elif self.nome == "Sex Education":
            print(
                f"{serie3.nome}: Série recomendada para adolescentes verem que sexo não é um tabu e a serie {serie3.nome} está disposta a discutir o tema.")

        else:
            print("Sem opniao cadastrada sobre a serie")




if __name__ == "__main__":
    serie1 = serie("Round 6", 25.90, 2021)
    serie2 = serie("Supernatural", 9.90, 2005, 15, 38)
    serie3 = serie("Os Simpsons",  279.90, 1989, 33, 24)

    serie1.get_nome()
    serie1.get_valor()
    serie1.get_ano()
    serie1.get_temporada()
    serie1.get_duracao()

    serie2.get_nome()
    serie2.get_valor()
    serie2.get_ano()
    serie2.get_temporada()
    serie2.get_duracao()

    serie3.get_nome()
    serie3.get_valor()
    serie3.get_ano()
    serie3.get_temporada()
    serie3.get_duracao()

    print("+_+" * 30)
    serie1.get_opniao()
    serie2.get_opniao()
    serie3.get_opniao()
    print("+_+" * 30)
    print("-="*30)
    print(serie1.retorna_dados())
    print(serie2.retorna_dados())
    print(serie3.retorna_dados())
    print("-=" * 30)
    serie1.set_nome("Grey's Anatomy")
    serie1.set_valor(29.90)
    serie1.set_ano(2005)
    serie1.set_temporada(18)
    serie1.set_duracao(42)

    serie2.set_nome("The Boys")
    serie2.set_valor(10)
    serie2.set_ano(2019)
    serie2.set_temporada(2)
    serie2.set_duracao(55)

    serie3.set_nome("Sex Education")
    serie3.set_valor(30)
    serie3.set_ano(2019)
    serie3.set_temporada(3)
    serie3.set_duracao(50)
    print("-=" * 30)
    print(serie1.retorna_dados())
    print(serie2.retorna_dados())
    print(serie3.retorna_dados())
    print("-="*30)

    serie1.compara_valor(serie2)
    serie1.compara_valor(serie3)
    serie2.compara_valor(serie3)

    print("+_+"*30)
    serie4 = serie("Hermanoteu", 2.50)
    serie1.get_opniao()
    serie2.get_opniao()
    serie3.get_opniao()
    serie4.get_opniao()


