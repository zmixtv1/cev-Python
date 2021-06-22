def leiaInt(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError, TypeError):
            print("\033[31mErro: por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número.\033[m ")
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n=float(input(msg))
        except(ValueError,TypeError):
            print("\033[31mErro: pro favor, digite um número real válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return n


n1 = leiaInt("Digite um Inteiro: ")
n2 = leiaFloat(("Digite um Real: "))
print(f"O valor digitado Inteiro foi {n1} e o valor Real é {n2}")

