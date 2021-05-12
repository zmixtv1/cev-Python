from random import randint
from time import sleep
computador = randint(0, 10)
print('-❤-' * 14)
print('Vou pensar em um numero entre 0 e 10. tente adivinhar!! ')
print('-❤-' * 14)
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2.5)
if jogador == computador:
    print('Parabêns!! você Ganhou!!')
else:
    print(f'Ganhei, eu pensei no numero {computador} e não no {jogador} ')
