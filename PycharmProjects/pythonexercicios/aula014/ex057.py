sexo = str(input("informe seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Dados invalidos. Por Favor, informe seu Sexo[M/F]: "))
print("Sexo validado com sucesso!")
