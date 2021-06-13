def tabuadas():
    num = int(input('Digite o número para a tabuada: '))
    arq_tabuada = open('f:\\z.doc\\tabuada.txt', 'w')
    for i in range(1, 11):
        arq_tabuada.write(f'{num} x {i} = {num * i} \n')
    arq_tabuada.write('\r')
    arq_tabuada.close()


def imprimir():
    arq_tabuada = open('f:\\z.doc\\tabuada.txt', 'r')
    for c in arq_tabuada:
        print(f"{c}", end="")
    arq_tabuada.close()


tabuadas()

imprimir()

