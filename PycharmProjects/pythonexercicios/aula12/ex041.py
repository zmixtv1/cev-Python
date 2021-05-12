from datetime import date
nasc= int(input("Em que ano você nasceu? "))
idade = date.today().year - nasc

if idade <= 9:
    print("Categoria Mirim")
elif idade <= 14:
    print("Categoria Infantil")
elif idade <= 19:
    print("categoria Junior")
elif idade <= 20:
    print("Categoria Sênior")
else:
    print("Master")

