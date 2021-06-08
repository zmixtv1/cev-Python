'''
def contador(i,f,p):
    """
    ->faz uma contafem e mostra na tela
    :param i: inicio da contagem
    :param f: Fim da contagem
    :apram p: Passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f"{c}",end=" ")
        c += p
    print("Fim")


contador(0, 100, 10)
help(contador)
'''


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f"A soma vale {s}")


somar(3, 2, 5)
somar(8, 4)
somar()
