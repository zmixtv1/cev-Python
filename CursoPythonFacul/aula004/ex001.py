'''from datetime import date

nome = str(input("Qual seu nome: "))
print(f"Boa Noite, {nome}")

nasc = int(input("Qual seu ano de nascimento: "))
idade = date.today().year - nasc
print(f"você tem {idade} anos! ")

nome = str(input("Qual seu nome: "))
nasc = int(input("Qual o ano de nascimento: "))
idade = date.today().year - nasc

print(f"Olá, seu nome é {nome} e tem {idade} anos!")

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

print(frase.replace("python", "goiaba"))
print(frase[4])
print(frase.upper())
print(frase.lower())
frase = "não estou gostando do curso"
print(frase.replace("não", " "))
'''
'''
#1
n1 = int(input("Digite um valor: "))
n2 = int(input("Digita outro valor: "))
if n1 > n2:
    print(f"{n1} é maior")
elif n2 > n1:
    print(f"{n2} é maior")
else:
    print("São iguais")
#2
num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))
num3 = int(input("Digite outro valor: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} é o maior número")
elif num2 > num1 and num2 > num3:
    print(f"{num2} é o maior número")
else:
    print(f"{num3} é o maior")

#3

n1 = int(input("Digite um valor: "))
if n1 % 2 == 0:
    print("O numero é par")
else:
    print("o numero é impar!")
'''
#4
media = 0
nota= ""
for x in range(3):
    nota = int(input(f"Digite a {x+1}ª nota: "))
    if nota > 0 and nota < 10:
        nota *= (x + 1)
        media += nota
    else:
        print("Digita um valor valido")
        break
ponderada = media / 6
if ponderada < 7:
    print("Você REPROVADO")
else:
    print("Você esta APROVADO")

print(ponderada)
