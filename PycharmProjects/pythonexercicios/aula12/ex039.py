from datetime import date
nascimento = int(input("Qual o ano que você nasceu? "))
alistamento = date.today().year - nascimento

if alistamento < 18:
    print("Você ainda irá se alistar!")
    saldo = 18 - alistamento
    if saldo == 1:
        print("Você terá que se alistar daqui {} ano".format(saldo))
    else:
        print("Você terá que se alistar daqui {} anos".format(saldo))
elif alistamento > 18:
    saldo = alistamento - 18
    print("Você deveria ter se alistado!")
    if saldo == 1:
        print("Deveria ter se alistado a {} ano".format(saldo))
    else:
        print("Deveria ter se alistado a {} anos".format(saldo))
else:
    print("Esta na hora de se alistar!!")

