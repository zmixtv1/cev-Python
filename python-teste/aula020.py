def men(msg):
    print("-" * 30)
    print(f"{msg:^30}")
    print("-" * 30)

men("Olá, Mundo")
men("Aprenda PYTHON")
men("Python é Muito Bom")


def soma(a, b):
    print(f" A = {a} B = {b}")
    s = a + b
    print(f"A Soma de A + B = {s}")


soma(4, 5)
soma(8, 9)
soma(2, 1)


def contador(*num):

    for valor in num:
        print(f"{valor}", end=" ")
    print("Fim")


contador(2, 1, 7)  
contador(8, 0)
contador(4, 4, 7, 6, 2)


def DV(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
DV(valores)
print(valores)

