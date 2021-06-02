aluno = {}
aluno["nome"] = str(input("Nome: "))
aluno["Média"] = float(input("Média: "))


print(f"nome é igual a {aluno['nome']}")
print(f"Média é igual a {aluno['Média']}")
if aluno["Média"] >= 7:
    print("Situação é igual a Aprovado.")
else:
    print("Situação é igual a Reprovado.")
