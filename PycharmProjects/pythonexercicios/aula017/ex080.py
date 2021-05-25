lista = []
for c in range(0, 5):
    valor = int(input("Digite um valor: "))
    if c == 0 or c > lista[-1]:
        lista.append(valor)

    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                break
            pos += 1

print(f"Os valores digitados em ordem foram {lista}!")