masc = fem = maior = 0
menor = 3
print("Digite [0] para sair")
while True:
    altura = float(input("Digite a altura: "))
    if altura == 0:
        break
    genero = input("[M]Para Masculino\n[F]para Feminino\nDigite: ").upper()
    if genero == "M":
        masc += 1
    else:
        fem += 1
    if altura > maior:
        maior = altura
    if altura < menor:
        menor = altura

print(f"Maior altura no grupo: {maior}")
print(f"Menor altura no grupo: {menor}")
print(f"Quantidade de homens: {masc}")
print(f"Quantidade de mulheres: {fem}")
