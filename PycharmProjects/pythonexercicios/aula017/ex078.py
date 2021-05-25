valores = list()
mai = men = 0
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
    if cont == 0:
        mai = men = valores[cont]
    else:
        if valores[cont] > mai:
            mai = valores[cont]
        if valores[cont] < men:
            men = valores[cont]

for c, v in enumerate(valores):
    print(f" Na posição {c} o valor é {v}!")

print(f"o menor valor foi digitado foi {mai} na posição ", end="")
for i, v, in enumerate(valores):
    if v == mai:
        print(f"{i}...", end=" ")
print()
print(f"O maior valor digitado foi {men} na posição", end=" ")
for i, v in enumerate(valores):
    if v == men:
        print(f"{i}...", end=" ")
print()
