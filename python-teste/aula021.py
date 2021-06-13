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

'''
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f"A soma vale {s}")


somar(3, 2, 5)
somar(8, 4)
somar()
'''

'''
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")


a= 5
teste(a)
print(f"A fora vale {a}")
'''

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f"Meus cáuculos deram {r1}, {r2}, {r3}")
