print('_✨_'*20)
print('Olá vamos fazer uma contagem de um número à outro!!')
print('Observação: Os números para digitar tem que ser inteiro e positivo!!!')
print('_✨_'*20)

n1 = int(input('Digite o número para começar a contagem:'))
n2 = int(input('Digite outro número para terminar a contagem:'))
n3 = int(input('Digite outro número para pular entre as contagens:'))

numeros1 = list(range(n1, (n2) + 1, n3))
from time import sleep
for contar in numeros1:
    sleep(0.3)
    print(contar)
