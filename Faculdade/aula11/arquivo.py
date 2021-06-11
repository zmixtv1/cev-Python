def tabuadas():
    num = int(input('Digite o número para a tabuada: '))
    arq_tabuada = open('c:\\temp\\tabuada.txt', 'w')
    for i in range(1, 11):
        arq_tabuada.write(f'{num} x {i} = {num * i} \n')
    arq_tabuada.write('\r')
    arq_tabuada.close()


def imprimir():
    arq_tabuada = open('c:\\temp\\tabuada.txt', 'r')
    print("-=" * 10)
    print(f'{"Tabuada" :^21}')
    for c in arq_tabuada:
        print(f"{c}", end="")
    print("-=" * 10)
    arq_tabuada.close()


tabuadas()
imprimir()


