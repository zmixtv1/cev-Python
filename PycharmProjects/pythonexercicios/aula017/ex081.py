lista = []
lista.append(int(input("Digite um valor: ")))
resp = str(input("Quer continuar [S/N]: ")).upper()
Nd = 0
while True:
    lista.append(int(input("Digite um valor: ")))
    resp = str(input("Quer continuar [S/N]: ")).upper()
    if resp == "S":
        Nd += 1
    else:
        break
print(f'A) {len(lista)} valores foram digitados!')
lista.sort(reverse=True)
print(f"B) Lista de valores oredenada de forma decrescente: {lista}")
if 5 in lista:
    print("O valor 5 se encontra dentro da lista!")
else:
    print("o valor 5 não se encontra dentro da lista!")
