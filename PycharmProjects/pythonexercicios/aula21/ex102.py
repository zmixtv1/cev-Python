def fatorial(num=1, show = False):
    """
    Calcula o fatorial de um numero.
    :param n: O numero a ser calculado.
    :param show: (opcional) mostra ou não a conta.
    :return: O valor di fatirual de um número n.
    """
    f = 1
    for c in range(num, 0,-1):
        if show:
            print(c, end="")
            if c >1:
                print(f"{c} x ", end=" ")
            else:
                print(" =", end=" ")
        f *= c
    return f

menu = str(input("Quer ajuda [S/N]: ")).upper()[0]
if menu == "S":
    help(fatorial)

f1 = int(input("Digite um valor: "))
cont = str(input("Quer que mostra a conta [S/N]: ")).upper()[0]

if cont == "S":
    print(fatorial(5, show= True))
else:
    print(fatorial(5))