from random import randint
from time import sleep
computador = randint(0, 10)
print('Vou pensar em um numero entre 0 e 10. tente adivinhar!! ')
jogador = ""
vezes = 0
while jogador != computador:
    jogador = int(input('Em que número eu pensei? '))
    print('Processando...')
    sleep(1)
    vezes += 1
    if jogador == computador:
        print("Parabens voce acertou, porem você precisou de {} tentativas".format(vezes))
    else:
        print("Errou tente novamente!")
