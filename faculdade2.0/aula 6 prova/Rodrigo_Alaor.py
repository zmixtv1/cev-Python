
'''
a. Crie uma lista vazia e acrescente alguns valores numéricos usando pelo menos dois métodos diferentes.
b. Calcule o mostre a média dos valores na lista.
c. Calcule o mostre a porcentagem dos valores negativos na lista.
d. Elabore mais um enunciado e a implementacão de mais uma questão na lista criada. Não faca exercício igual aos
ministrados nas aulas. A complexidade do enunciado e da implementacão da questão serão considerados para mensurar a avaliacão da questão.
- Vale 40%
'''


a = list()
a.insert(10, 2)
a.append(10)
media = sum(a) / len(a)
quant = 0
for c in range(0, len(a)):
    if a[c] < 0:
        quant += 1
print(a)
print(media)
porcentagem = (quant / len(a)) * 100
print(media)

'''
d. Elabore mais um enunciado e a implementacão de mais uma questão na lista criada.
 Não faca exercício igual aos ministrados nas aulas. A complexidade do enunciado e da 
 implementacão da questão serão considerados para mensurar a avaliacão da questão.
- Vale 40%
'''


'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
 mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

valores = list()
mai = men = 0
for cont in range(0, 5):
    valores.append(int(input(f"Digite {cont}° valor: ")))
    if cont == 0:
        mai = men = valores[cont]
    else:
        if valores[cont] > mai:
            mai = valores[cont]
        if valores[cont] < men:
            men = valores[cont]

for c, v in enumerate(valores):
    print(f" Na posicão {c} o valor é {v}!")

print(f"o menor valor foi digitado foi {mai} na posicão ", end="")
for i, v, in enumerate(valores):
    if v == mai:
        print(f"{i}...", end=" ")
print()
print(f"O maior valor digitado foi {men} na posicão", end=" ")
for i, v in enumerate(valores):
    if v == men:
        print(f"{i}...", end=" ")
print()










class livro(object):
    def __init__(self,titulo,autor,paginas,preco=100,quantidade=1):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.quantidade = quantidade
        self.preco = preco

    def get_quantidade(self):
        return self.quantidade


    def set_quantidade(self, no_quantidade):
        self.quantidade = no_quantidade
        if self.quantidade == 0:
            print("Livro em falta!")

    def aumento_preco(self,novo_preco):
        self.preco = novo_preco


    '''Faça um metodo para que a quantidade de livros for superior a 50 dê 50% de desconto
    e superior a 30 de 15% de desconto'''
    def desconto(self):
        if self.quantidade >= 50:
            porcentagem = 0.5
            self.preco *= 1 - porcentagem
            print(f"desconto de ",self.preco)
        elif self.quantidade >= 30:
            self.preco *= 1 - 0.15
            print(f"desconto de ",self.preco)

if __name__ == "__main__":
    livro1 = livro("Harry Potter","JK.Roling",500,500,30)
    livro2 = livro("Python","Rodrigo",200)

    livro1.get_quantidade()
    livro2.get_quantidade()

    livro1.set_quantidade(40)
    livro2.set_quantidade(60)

    livro1.aumento_preco(1000)
    livro2.aumento_preco(500)

    livro1.desconto()
    livro2.desconto()
