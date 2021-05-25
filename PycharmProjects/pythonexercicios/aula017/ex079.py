'''
valores = []

while True:
    valores.append(int(input("Digite um valor: ")))
    resp = str(input("Quer continuar[S/N]: ")).upper()
    if resp == "S":
        valores.append(int(input("Digite outro valor: ")))
        resp = str(input("Quer continuar[S/N]: ")).upper()
    else:
        break
valores.sort()
print(f"você digitou os valores {valores}")
'''

valores = []
while True:
    n = int(input("Digite um valor: "))
    if n not in valores:
        valores.append(n)
    else:
        print("valor duplicado! Não vou adicionar...")
    r= str(input("Quer continuar [S/N]: "))
    if r in "Nn":
        break
valores.sort()
print(f"você digitou os valores {valores}")