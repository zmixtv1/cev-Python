def area(larg, comp):
    area = larg * comp
    print(f"A area do terreno {larg} X {comp} é de {area}M²")


def msg():
    print("-" * 40)
    print(f"{'Controle de terrenos:':^40}")
    print("-" * 40)

msg()
l = float(input("Qual a dimensão da largura (M): "))
c = float(input("Qual a dimensão do comprimento (M): "))
area(l, c)
