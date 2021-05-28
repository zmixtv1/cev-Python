matriz = [[0, 0, 0],  [0, 0, 0],  [0, 0, 0]]
totalpar = soma3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f"Digite um valor para[{l}, {c}]: "))
        matriz[l][c] = valor
        if valor % 2 == 0:
            totalpar += valor
        if matriz[l][2] != 0:
            soma3 += valor
        if matriz[1][c] >= maior:
            maior = matriz[1][c]
print("_-" * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()
print(f"A soma de todos os valores pares digitados é: {totalpar}")
print(f"A soma dos valores da terceira coluna é: {soma3}")
print(f"O maior valor da segunda linha é: {maior}")

