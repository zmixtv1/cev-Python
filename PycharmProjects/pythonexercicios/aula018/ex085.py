lista = [[], []]
valor = 0
for c in range(0, 7):
    valor = (int(input(f"Digite o {c+1}° valor: ")))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print("-_" * 20)
print(f"Lista total{lista}")
lista[0].sort()
print(f"Os valores pares digitados foram {lista[0]}")
lista[1].sort()
print(f"Os valores impares digitados foram {lista[1]}")
