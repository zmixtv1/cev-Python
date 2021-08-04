nota = valor = media = aluno = 0

while True:
    if nota == -1:
        break
    else:
        if valor == 0:
            nota = float(input("Digite a nota do aluno [-1]SAIR: "))
            if nota != -1:
                valor += nota
                aluno += 1
        else:
            nota = float(input("Digite a nota do outro aluno [-1]SAIR: "))
            if nota != -1:
                valor += nota
                aluno += 1
media = valor/aluno
print(f"A média da Turma é de {media}")
