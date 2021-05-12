from datetime import  date
from time import sleep
print('-=-'*30)
print('Vamos Calcular se o ano digitado é bixesto ou não!')
print('-=-'*30)
ano = int(input('Que ano quer analisar: '))
print('Processando...')
sleep(1)
if ano ==0:
    ano = date.today().year
bissexto = ano % 4
if bissexto == 0 and bissexto % 100 !=0 or ano % 400 == 0:
    print('O ano {} é bissexto!!'.format(ano))
else:
    print('O ano {} NÃO é bissexto!!'.format(ano))
