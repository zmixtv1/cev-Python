import sys
maior = 0
menor = sys.maxsize
while True:
    núm = int(input("Digite um numero: "))
    if núm < 0:

        break
    else:
        if núm >= núm:
            maior = núm
        if núm <= menor:
            menor = núm
print(f"O maior número digitado foi {maior}\nO menor número digitado foi {menor}!")