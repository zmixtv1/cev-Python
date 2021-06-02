import datetime
while True:
    nome = str(input("Nome: "))
    nasc = int(input("Ano de Nascimento: "))
    trab = int(input("Carteira de Trabalho (0não tem): "))
    idade = datetime.date.today().year - nasc
    if trab == 0:
        dados1 = {"Nome": nome, "Idade": idade, "CTPS": trab}
        break
    else:
        contra = int(input("Ano de Contratação: "))
        salario = float(input("Salário: R$ "))
        aposentadoria = idade + ((contra + 35) - datetime.date.today().year)
        dados = {"Nome": nome,
                 "Idade": idade,
                 "CTPS": trab,
                 "Contratação": 1995,
                 "Salário": salario,
                 "Aposentadoria": aposentadoria}

        break
print("-=" * 30)
if trab == 0:
    for k, v in dados1.items():

        print(f"{k} tem o valor: {v}")
    print(dados1)
else:
    for k, v in dados.items():

        print(f"{k} tem o valor: {v}")
    print(dados)

