from datetime import date

'''nome = str(input("Qual seu nome: "))
print(f"Boa Noite, {nome}")

nasc = int(input("Qual seu ano de nascimento: "))
idade = date.today().year - nasc
print(f"você tem {idade} anos! ")

nome = str(input("Qual seu nome: "))
nasc = int(input("Qual o ano de nascimento: "))
idade = date.today().year - nasc

print(f"Olá, seu nome é {nome} e tem {idade} anos!")
'''
soma = num = media = valor = 0
nota = 1
for c in range(0, 3):
    if valor >= 0 and valor <= 10:
        valor = float(input(f"Digite a {nota}ª nota: "))
        nota += 1
        soma += valor
        num += 1
        media = soma / num
    else:
        print("Digite um valor valido")
        media = 0
        break
print(f"A media do aluno é de {media}")
'''
oposto = float(input("Digite o valor do cateto oposto: "))
adjascente = float(input("Digite o valor do cateto adjascente: "))
hipotenusa = float(input("Digite o valor da hipotenusa: "))

sen = oposto / hipotenusa
cos = adjascente / hipotenusa
tg = oposto / adjascente

print(f"O sen dos agulos é {sen}")
print(f"O Cos dos angulos é {cos}")
print(f"A tag dos angulos é {tg}")



n1 = int(input("Digite um numero: "))
pot = n1 ** 2
print(f"O valor da conta é {pot % 3}")


frase = str(input("Digite uma frase: "))
print(len(frase))

print(frase.replace("pyhon"))
print(frase[4])
print(frase.upper())
print(frase.lower())
'''

