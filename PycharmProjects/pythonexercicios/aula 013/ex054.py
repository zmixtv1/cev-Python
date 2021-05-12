from datetime import date
atual = date.today().year
totmair = 0
totmenor = 0
for c in range(0, 7):
    nasc = int(input("Em que ano a pessoa nasceu? "))
    idade = atual - nasc

    if idade >= 21:

        totmair += 1
    else:
        totmenor += 1

print(" {} dessas pessoas não atigiram a maioridade, {} já".format(totmair, totmenor))
