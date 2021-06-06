from time import sleep


def contador(i, f, p):
    print(f"Contagem de {i} até {f} de {p} em {p}")
    sleep(2.5)
    for c in range(i, f + 1, p):
        print(c, end=" ", flush=True)
        sleep(0.3)
    print()
    if i >= f:
        p = -p

        for a in range(i, f-1, p):
            print(a, end=" ", flush=True)
            sleep(0.3)
        print()


contador(1, 10, 1)
print("_" * 30)
contador(10, 0, 2)
print("_" * 30)
print("Agora é sua vez de personalizar a contagem!")
a = int(input("Início: "))
b = int(input("Fim: "))
c = int(input("Passo: "))
if c == 0:
    c = 1
if c < 0:
    c = -c
contador(a, b, c)
