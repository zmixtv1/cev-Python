lista = []

while True:
    nome = str(input("Nome: ")).capitalize()
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2
    resp = str(input("Quer continuar[S/N]: ")).upper()
    lista.append([nome, [n1, n2], media])
    if resp in "N":
        break
for i, l in enumerate(lista):
    print(f"{i+1}ª aluno: {l[0]}\n\033[0:31m1°nota:\033[m {l[1][0]} \033[0:31m2°nota:\033[m {l[1][1]}\nA media do aluno foi de {l[2]}")
    print("-=" * 16)
print("       <<<volte sempre!>>>          ")