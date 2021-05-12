from random import randint
cont = 0
while True:
    valor = int(input("Digite um valor: "))
    conputador = randint(0, 10)
    total = conputador + valor
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou Impar [P/I]")).strip().upper()[0]
    print(f"você jogou {valor} e o computador {conputador}")
    print("Deu Par " if total % 2 == 0 else "Deu impar")
    if tipo == "P":
        if total % 2 == 0:
            print("Você venceu!")
            cont += 1
        else:
            print("Você Perdeu!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você Venceu!")
            cont += 1
        else:
            print("Você Perdeu!")
            break
    print("Vamos jogar novamente...")
print(f"Você venceu {cont} vezes!")