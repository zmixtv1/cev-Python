n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = n1 + n2 / 2
print("Sua média é de {}".format(media))
if media < 4.9:
    print("Que pena você reprovou!")
elif media >= 5.0 and  media <= 6.9:
    print("Você esta em recuperação!")
else:
    print("Você foi aprovado!")
